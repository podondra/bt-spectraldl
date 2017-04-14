import spectraldl.utils


def test_retrieve_url():
    data = spectraldl.utils.retrieve_url('http://httpbin.org')
    assert data != ''
