import numpy as np
import pytest


def run_test(metric="l2", dtype=np.float32):
    import pynanoflann

    n_batches = 100
    target = np.random.rand(n_batches, 10000, 3).astype(dtype)
    query = np.random.rand(n_batches, 2000, 3).astype(dtype)

    g_res_d = []
    g_res_i = []
    for i in range(n_batches):
        kd_tree = pynanoflann.KDTree(n_neighbors=4, metric=metric, leaf_size=20)
        kd_tree.fit(target[i])
        d, nn_idx = kd_tree.kneighbors(query[i])
        g_res_d.append(d)
        g_res_i.append(nn_idx)

    g_res_d = np.array(g_res_d)
    g_res_i = np.array(g_res_i)

    distances, indices = pynanoflann.batched_kneighbors(
        target, query, n_neighbors=4, metric=metric, leaf_size=20, n_jobs=2
    )
    distances = np.array(distances)
    indices = np.array(indices)

    assert np.allclose(g_res_d, distances)
    assert (indices == g_res_i).all()


def test_bached32():
    run_test(dtype=np.float32)


def test_bached64():
    run_test(dtype=np.float64)


def test_bad_metric():
    with pytest.raises(ValueError):
        run_test(metric="l0")
