import random
from datetime import datetime, timedelta



def generate_birth_date(start_year=1900, end_year=2022) -> str:
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    birth_date = start_date + timedelta(days=random_days)
    return birth_date.strftime('%y%m%d')

def generate_place_of_birth():
    place_codes = [
        '01', '21', '22', '23', '24',  # Johor
        '02', '25', '26', '27',        # Kedah
        '03', '28', '29',              # Kelantan
        '04', '30',                    # Malacca
        '05', '31', '59',              # Negeri Sembilan
        '06', '32', '33',              # Pahang
        '07', '34', '35',              # Penang
        '08', '36', '37', '38', '39',  # Perak
        '09', '40',                    # Perlis
        '10', '41', '42', '43', '44',  # Selangor
        '11', '45', '46',              # Terengganu
        '12', '47', '48', '49',        # Sabah
        '13', '50', '51', '52', '53',  # Sarawak
        '14', '54', '55', '56', '57',  # FT of Kuala Lumpur
        '15', '58',                    # FT of Labuan
        '16',                          # FT of Putrajaya
        '60',                          # Brunei
        '61',                          # Indonesia
        '62',                          # Cambodia
        '63',                          # Laos
        '64',                          # Myanmar
        '65',                          # Philippines
        '66',                          # Singapore
        '67',                          # Thailand
        '68',                          # Vietnam
        '69', '70', '73', '80', '81',  # N/A
        '71', '72',                    # Born outside Malaysia prior to 2001
        '74',                          # China
        '75',                          # India
        '76',                          # Pakistan
        '77',                          # Saudi Arabia
        '78',                          # Sri Lanka
        '79',                          # Bangladesh
        '82',                          # Unknown state
        '83',                          # Various Asia-Pacific countries
        '84'                           # Various South American countries
    ]
    return random.choice(place_codes)

def generate_random_number(is_male=True):
    random_number = random.randint(0, 999)
    last_digit = random.choice(
        [1, 3, 5, 7, 9]) if is_male else random.choice([0, 2, 4, 6, 8])
    return f'{random_number:03d}{last_digit}'

def generate_mykad(num_mykad):
    """Generates a Malaysia identifier number (MyKad)."""
    mykad = []
    for _ in range(num_mykad):
        dob = generate_birth_date()
        pob = generate_place_of_birth()
        gender = random.choice([True, False])  # True for male, False for female
        random_num = generate_random_number(gender)
        id_number = f'{dob}-{pob}-{random_num}'
        mykad.append(id_number)
    return mykad