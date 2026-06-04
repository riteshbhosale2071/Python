def notebook():
    notebooks = int(input("Enter number of notebooks: "))
    
    pages_per_notebook = int(input("Enter pages in each notebook: "))

    total_pages = notebooks * pages_per_notebook

    print("Total Pages =", total_pages)

notebook()