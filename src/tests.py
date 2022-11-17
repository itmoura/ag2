import pytest
from main import prediction

# Risco de crédito
# ruim = 0 (Aprovado)
# bom = 1 (Reprovado)

def contruct_credit_data(status, duration, credit_history, purpose, amount, savings, employment_duration, installment_rate, personal_status_sex, other_debtors, present_residence, property, age, other_installment_plans, housing, number_credits, job, people_liable, telephone, foreign_worker):
  return {
    'status': status,
    'duration': duration,
    'credit_history': credit_history,
    'purpose': purpose,
    'amount': amount,
    'savings': savings,
    'employment_duration': employment_duration,
    'installment_rate': installment_rate,
    'personal_status_sex': personal_status_sex,
    'other_debtors': other_debtors,
    'present_residence': present_residence,
    'property': property,
    'age': age,
    'other_installment_plans': other_installment_plans,
    'housing': housing,
    'number_credits': number_credits,
    'job': job,
    'people_liable': people_liable,
    'telephone': telephone,
    'foreign_worker': foreign_worker
  }

def predict_value(credit_data, result):
  assert prediction(credit_data) == result

def test_prediction():
  predict_value(contruct_credit_data(1, 18, 4, 2, 1049, 1, 2, 4, 2, 1, 4, 2, 21, 3, 1, 1, 3, 2, 1, 2), 1)
  predict_value(contruct_credit_data(1, 9, 4, 0, 2799, 1, 3, 2, 3, 1, 2, 1, 36, 3, 1, 2, 3, 1, 1, 2), 1)
  #predict_value(contruct_credit_data(2, 12, 2, 3, 6468, 5, 1, 2, 3, 1, 1, 4, 52, 3, 2, 1, 4, 2, 2, 2), 0)
  predict_value(contruct_credit_data(1, 30, 2, 2, 6350, 5, 5, 4, 3, 1, 4, 2, 31, 3, 2, 1, 3, 2, 1, 2), 0)
