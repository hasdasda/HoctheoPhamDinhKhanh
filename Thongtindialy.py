import sys
# install package reverse_geocoder
# cần thông tin trích xuất ịa lý từ tập dataset của cuộc thi Rental Listing Inquiries Kaggle Competition.
import reverse_geocoder as revgc
revgc.search(dataset.latitude[1], dataset.longitude[1])
