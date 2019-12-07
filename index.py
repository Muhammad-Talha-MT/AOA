import pandas as pd


def dataPreProcessing():
    shoes_data = pd.read_csv('Datafiniti_Womens_Shoes_Jun19.csv')
    rows, columns = shoes_data.shape
    categories_set = set()
    shoes_url = {}
    shoe_categories = {}
    brand_set = set()
    shoe_brand = {}
    for i in range(rows):
        category = shoes_data.loc[i, 'categories'].split(',')
        brand_set.add(shoes_data.loc[i, 'brand'])
        shoe_brand[i] = shoes_data.loc[i, 'brand']
        shoes_url[i] = shoes_data.loc[i, 'sourceURLs']
        shoe_categories[i] = category
        for c in category:
            categories_set.add(c)

    categories_list = list(categories_set)
    brand_list = list(brand_set)
    new_columns = categories_list + brand_list
    new_columns.append('shoes_id')
    df_shoes = pd.DataFrame(index=range(rows), columns=new_columns)
    df_shoes = df_shoes.fillna(0)
    for i in range(rows):
        df_shoes.loc[i, 'shoes_id'] = shoes_data.loc[i, 'id']
        for column in new_columns:
            if column in shoe_categories[i]:
                df_shoes.loc[i, column] = 1
            if column == shoe_brand[i]:
                df_shoes.loc[i, column] = 1

    df_shoes.to_csv('data.csv')


def main():
    dataPreProcessing()


if __name__ == '__main__':
    main()
