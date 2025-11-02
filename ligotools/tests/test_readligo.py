from ligotools import readligo as rl
import pytest

def test_read_frame_ifo_TypeError():
    """If ifo not provided, read_frame should raise TypeError"""
    with pytest.raises(TypeError):
        rl.read_frame('test.gwf', ifo=None)

def test_loaddata_no_file_return_None():
    """If the file does not exist, loaddata should return (None, None, None)"""
    output = rl.loaddata('nonexistent_file.hdf5', ifo='H1')
    expected = (None, None, None)
    assert output == expected