from models.buku_model import BukuModel

def test_get_all_buku():
    model = BukuModel()
    result = model.get_all_buku()
    
    # Memastikan bahwa hasil mengembalikan sebuah list (atau data dari database)
    assert isinstance(result, list)