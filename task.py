def merge_lists_to_dict(a, b):
    combined_data = zip(a, b)
    result_dict = dict(combined_data)
    return result_dict


products = ["Book", "Pen", "Notebook", "Pencil"]
prices = [150, 30, 80, 20]

product_dictionary_keyword = merge_lists_to_dict(a=products, b=prices)
print(f"Dictionary using keyword arguments: {product_dictionary_keyword}")

product_dictionary_mixed = merge_lists_to_dict(products, b=prices)
print(f"Dictionary using mixed arguments: {product_dictionary_mixed}")
