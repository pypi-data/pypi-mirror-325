use kdtree::distance::squared_euclidean;
use kdtree::KdTree;
use numpy::ndarray::{Array1, Array2};
use numpy::{IntoPyArray, PyArray1, PyArray2, PyArrayMethods, PyReadonlyArray1, PyReadonlyArray2};
use ordered_float::OrderedFloat as F;
use pyo3::prelude::*;
use pyo3::types::PyType;
use rangemap::RangeMap;
use rayon::prelude::*;
use skymask_rs::data::read_shp;
use skymask_rs::utils::{ProjLine, ProjSegment};

#[pyclass]
struct World {
    lines: Array2<f64>,
    kdtree: KdTree<f64, usize, [f64; 2]>,
    #[pyo3(get, set)]
    max_dist: f64,
    #[pyo3(get, set)]
    eps: f64,
}

#[pymethods]
impl World {
    #[new]
    #[pyo3(signature = (path, max_dist, eps = 1e-6))]
    fn new(path: &str, max_dist: f64, eps: f64) -> Self {
        let (lines, _, kdtree) = read_shp(path);
        Self {
            lines,
            kdtree,
            max_dist,
            eps,
        }
    }
    #[classmethod]
    #[pyo3(signature = (lines, max_dist, eps = 1e-6))]
    fn from_lines<'py>(
        _: &Bound<'py, PyType>,
        lines: PyReadonlyArray2<f64>,
        max_dist: f64,
        eps: f64,
    ) -> Self {
        let lines = lines.as_array();
        let mut kdtree = KdTree::new(2);
        lines.rows().into_iter().enumerate().for_each(|(idx, row)| {
            kdtree
                .add([(row[0] + row[3]) / 2.0, (row[1] + row[4]) / 2.0], idx)
                .unwrap();
        });
        Self {
            lines: lines.to_owned(),
            kdtree,
            max_dist,
            eps,
        }
    }
    #[getter]
    fn lines<'py>(this: Bound<'py, Self>) -> Bound<'py, PyArray2<f64>> {
        let lines = &this.borrow().lines;
        let res = unsafe { PyArray2::borrow_from_array(lines, this.into_any()) };
        res.readwrite().make_nonwriteable();
        res
    }
    fn skymask(&self, pos: [f64; 2]) -> SkymaskMap {
        let lines_iter = self
            .kdtree
            .within(&pos, self.max_dist.powi(2), &squared_euclidean)
            .unwrap()
            .into_iter()
            .filter_map(|(_, &i)| {
                let row = self.lines.row(i);
                ProjSegment::<F<f64>, (F<f64>, F<f64>)>::from_points(
                    &[F(row[0] - pos[0]), F(row[1] - pos[1]), F(row[2])],
                    &[F(row[3] - pos[0]), F(row[4] - pos[1]), F(row[5])],
                )
            });
        SkymaskMap(skymask_rs::skymask(lines_iter, F(self.eps)))
    }
    fn par_skymask(&self, pos: Vec<[f64; 2]>) -> Vec<SkymaskMap> {
        pos.into_par_iter().map(|pos| self.skymask(pos)).collect()
    }
    fn par_samples<'py>(
        &self,
        py: Python<'py>,
        pos: Vec<[f64; 2]>,
        samples: PyReadonlyArray1<f64>,
    ) -> Bound<'py, PyArray2<f64>> {
        let samples = samples.as_array();
        let shape = (pos.len(), samples.shape()[0]);
        let res = pos
            .into_par_iter()
            .flat_map(|pos| {
                self.skymask(pos)
                    .samples_iter(samples.iter())
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        Array2::from_shape_vec(shape, res).unwrap().into_pyarray(py)
    }
}

#[pyclass]
#[repr(transparent)]
struct SkymaskMap(RangeMap<F<f64>, (F<f64>, F<f64>)>);

impl SkymaskMap {
    fn samples_iter<'a>(
        &'a self,
        it: impl Iterator<Item = &'a f64> + 'a,
    ) -> impl Iterator<Item = f64> + 'a {
        it.map(|&x| self.at(x))
    }
}

#[pymethods]
impl SkymaskMap {
    fn at(&self, theta: f64) -> f64 {
        let theta = F(theta);
        self.0.get(&theta).map(|f| f.at(theta).0).unwrap_or(0.0)
    }
    fn samples<'py>(
        &self,
        py: Python<'py>,
        samples: PyReadonlyArray1<f64>,
    ) -> Bound<'py, PyArray1<f64>> {
        Array1::from_iter(self.samples_iter(samples.as_array().iter())).into_pyarray(py)
    }
    fn segments(&self) -> Vec<((f64, f64), (f64, f64))> {
        self.0
            .iter()
            .map(|(dom, &(F(a), F(b)))| ((dom.start.0, dom.end.0), (a, b)))
            .collect()
    }
}

#[pymodule]
fn skymask_py(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<World>()?;
    m.add_class::<SkymaskMap>()?;
    Ok(())
}
