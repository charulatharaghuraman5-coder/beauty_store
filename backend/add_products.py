import random

brands = ['GlowLab', 'RadiantSkin', 'PureGlow', 'ColorPop', 'FlawlessBeauty', 'GlamEyes', 'SilkHair', 'HairRevive', 'LuxeScent', 'AquaEssence', 'BodyBliss', 'TropicalGlow']
categories = ['Skincare', 'Makeup', 'Haircare', 'Fragrance', 'Bath and Body']

skincare_products = ['Face Serum', 'Night Cream', 'Day Cream', 'Face Wash', 'Toner', 'Face Mask', 'Eye Cream', 'Sunscreen', 'Moisturizer', 'Cleanser', 'Exfoliator', 'Face Oil', 'Essence', 'Ampoule', 'Sheet Mask', 'Peel', 'Scrub', 'Mist', 'Gel', 'Lotion']
makeup_products = ['Lipstick', 'Foundation', 'Concealer', 'Blush', 'Highlighter', 'Bronzer', 'Eyeshadow', 'Eyeliner', 'Mascara', 'Kajal', 'Lip Gloss', 'Lip Liner', 'Primer', 'Setting Spray', 'Compact', 'BB Cream', 'CC Cream', 'Contour', 'Brow Pencil', 'Nail Polish']
haircare_products = ['Shampoo', 'Conditioner', 'Hair Serum', 'Hair Oil', 'Hair Mask', 'Hair Spray', 'Hair Gel', 'Hair Cream', 'Hair Wax', 'Hair Mousse', 'Leave-in Conditioner', 'Dry Shampoo', 'Hair Tonic', 'Scalp Treatment', 'Hair Color', 'Hair Bleach', 'Hair Straightener Cream', 'Hair Curling Cream', 'Anti-Dandruff Shampoo', 'Hair Growth Serum']
fragrance_products = ['Perfume', 'EDT', 'EDP', 'Body Mist', 'Deodorant', 'Roll-on', 'Attar', 'Cologne', 'Body Spray', 'Fragrance Oil']
bath_products = ['Body Lotion', 'Body Wash', 'Body Scrub', 'Body Butter', 'Hand Cream', 'Foot Cream', 'Bath Salt', 'Shower Gel', 'Body Oil', 'Soap', 'Bath Bomb', 'Body Polish', 'Hand Wash', 'Foot Scrub', 'Body Mist', 'Talcum Powder', 'Body Serum', 'Massage Oil', 'Body Milk', 'Exfoliating Gloves']

adjectives = ['Hydrating', 'Nourishing', 'Brightening', 'Anti-Aging', 'Revitalizing', 'Soothing', 'Refreshing', 'Intensive', 'Gentle', 'Deep', 'Ultra', 'Premium', 'Luxury', 'Professional', 'Advanced', 'Natural', 'Organic', 'Herbal', 'Vitamin', 'Collagen', 'Peptide', 'Retinol', 'Hyaluronic', 'Ceramide', 'Niacinamide']

images = [
    "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400",
    "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400",
    "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400",
    "https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400",
    "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400",
    "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400",
    "https://images.unsplash.com/photo-1583241800698-c318c76ca7e6?w=400",
    "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400",
    "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400",
    "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400"
]

products = []
id_counter = 43

for brand in brands:
    for category in categories:
        if category == 'Skincare':
            product_list = skincare_products
        elif category == 'Makeup':
            product_list = makeup_products
        elif category == 'Haircare':
            product_list = haircare_products
        elif category == 'Fragrance':
            product_list = fragrance_products
        else:
            product_list = bath_products
        
        for i in range(20):
            adj = random.choice(adjectives)
            prod = random.choice(product_list)
            name = f"{adj} {prod}"
            price = random.randint(299, 2999)
            image = random.choice(images)
            
            products.append(f'{{id:{id_counter},name:"{name}",brand:"{brand}",category:"{category}",price:{price},image_url:"{image}"}}')
            id_counter += 1

print(',\n    '.join(products))
