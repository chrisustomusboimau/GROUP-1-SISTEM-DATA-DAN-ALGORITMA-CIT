#Validasi nilai yang diinputkan selalu dalam kisaran nilai yang ada (0-100)

def input_score():
    while True:
        insert_your_score = int(input("Enter your finalized score (0-100):"))
        if 0 <= insert_your_score <= 100:
            return insert_your_score
        else:
            print("What you've just inserted is not a valid score, please insert something in between 0 and 100")

final_score = input_score()

#Pengkriterian Nilai Akhir  Mahasiswa berdasarkan ketentuan penilaian terhadap nilai akhir
def final_score_to_grade_conversion(final_score):
    if 91 <= final_score <= 100:
        return "A (Distinctive)"
    elif 86 <= final_score <= 90:
        return "A (Excellent)"
    elif 81 <= final_score <= 85:
        return "B+ (Honorable)"
    elif 76 <= final_score <= 80:
        return "B (Very Good)"
    elif 71 <= final_score <= 75:
        return "B- (Good)"
    elif 61 <= final_score <= 70:
        return "C+ (Sufficient)"
    elif 51 <= final_score <= 60:
        return "C (Fairly Satisfactory)"
    elif 46 <= final_score <= 50:
        return "C- (Poor)"
    elif 41 <= final_score <= 45:
        return "D (Insufficient)"
    else:
        return "F (Failed)"

grade_criteria = final_score_to_grade_conversion(final_score)

print(f"With {final_score} as your final score, your grade for this subject is ({grade_criteria})")