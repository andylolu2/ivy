from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test


# random_sample
@handle_frontend_test(
    fn_tree="tensorflow.random.uniform",
    shape=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        min_value=1,
        max_value=5,
        min_num_dims=1,
        max_num_dims=1,
    ),
    minval=helpers.ints(min_value=0, max_value=3),
    maxval=helpers.ints(min_value=4, max_value=10),
    dtype=helpers.get_dtypes("float", full=False),
    seed=helpers.ints(min_value=0, max_value=10),
    test_with_out=st.just(False),
)
def test_tensorflow_uniform(
    shape,
    minval,
    maxval,
    dtype,
    seed,
    frontend,
    test_flags,
    fn_tree,
    on_device,
):

    input_dtypes, shape = shape
    helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        test_values=False,
        shape=shape[0],
        minval=minval,
        maxval=maxval,
        dtype=dtype[0],
        seed=seed,
    )
