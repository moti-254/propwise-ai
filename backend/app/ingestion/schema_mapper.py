COLUMN_MAPPING = {
    "price": ["price", "Price", "listing_price"],
    "location": ["location", "city", "town", "area"],
    "bedrooms": ["bedrooms", "bed", "beds"],
    "bathrooms": ["bathrooms", "bath", "baths"],
    "square_feet": ["square_feet", "house_size", "sqft", "area"],
    "expected_rent": ["rent", "monthly_rent", "price_per_month"],
    "property_type": ["property_type", "type"],
    "latitude": ["latitude", "lat"],
    "longitude": ["longitude", "lng", "lon"],
    "listing_description": ["description", "listing_description"],
}

def map_columns(df):
    rename_dict = {}
    for target_col, possible_cols in COLUMN_MAPPING.items():
        for col in possible_cols:
            if col in df.columns:
                rename_dict[col] = target_col
                break
    return df.rename(columns=rename_dict)
