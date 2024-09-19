from pdf2image import convert_from_path

# Convert the PDF to a list of images (one per page)
images = convert_from_path('../scripts/pypdf.pdf', dpi=300, output_folder='./output', fmt='png')

for i, image in enumerate(images):
    image.save(f'./output/page-{i}.png', 'PNG')
