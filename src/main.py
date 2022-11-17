import pandas as pd
import numpy as np
import pickle
import streamlit as st
import constants

# Carregando o modelo assets/credit_risk_model.sav
loaded_model = pickle.load(open('src/assets/credit_risk_model.sav', 'rb'))

# Função que recebe os dados do usuário e retorna a predição do modelo
def prediction(credit_data):
  df = pd.DataFrame(credit_data, index=[0])
  prediction = loaded_model.predict(df)
  return prediction[0]

# Função main que representa o front-end da aplicação
def main():
  # Elemementos da página
  html_temp = """
  <div style ="background-color:#2E6171;padding:13px;border-radius: 5px">
    <h1 style ="color:white;text-align:center;">Aplicativo para análise de crédito</h1>
  </div>
  """

  # Mostrando o aspecto da página
  st.markdown(html_temp, unsafe_allow_html = True)

  # Criando os campos de entrada para o usuário preencher com os dados
  status = st.selectbox('Status', constants.CreditData.STATUS)
  duration = st.number_input('Duração (em meses)', min_value=1, max_value=100, value=1)
  credit_history = st.selectbox('Histórico de crédito', constants.CreditData.CREDIT_HISTORY)
  purpose = st.selectbox('Propósito', constants.CreditData.PURPOSE)
  amount = st.number_input('Valor do crédito (em DM)')
  savings = st.selectbox('Poupança', constants.CreditData.SAVINGS)
  employment_duration = st.selectbox('Duração do emprego', constants.CreditData.EMPLOYMENT_DURATION)
  installment_rate = st.selectbox('Taxa de parcelamento', constants.CreditData.INSTALLMENT_RATE)
  personal_status_sex = st.selectbox('Status pessoal', constants.CreditData.PERSONAL_STATUS_SEX)
  other_debtors = st.selectbox('Outros devedores', constants.CreditData.OTHER_DEBTORS)
  present_residence = st.selectbox('Tempo de residência', constants.CreditData.PRESENT_RESIDENCE)
  property = st.selectbox('Propriedade', constants.CreditData.PROPERTY)
  age = st.number_input('Idade (em anos)', min_value=18, max_value=100, value=18)
  other_installment_plans = st.selectbox('Outros planos de parcelamento', constants.CreditData.OTHER_INSTALLMENT_PLANS)
  housing = st.selectbox('Habitação', constants.CreditData.HOUSING)
  number_credits = st.selectbox('Número de créditos', constants.CreditData.NUMBER_CREDITS)
  job = st.selectbox('Trabalho', constants.CreditData.JOB)
  people_liable = st.selectbox('Pessoas a cargo', constants.CreditData.PEOPLE_LIABLE)
  telephone = st.selectbox('Telefone', constants.CreditData.TELEPHONE)
  foreign_worker = st.selectbox('Trabalhador estrangeiro', constants.CreditData.FOREIGN_WORKER)
  result =""

  # Quando o botão 'Analisar' for clicado, a função 'prediction' será chamada e o resultado será mostrado
  if st.button("Analisar"):
    credit_data = {
      'status': constants.CreditData.STATUS.index(status) + 1,
      'duration': duration,
      'credit_history': constants.CreditData.CREDIT_HISTORY.index(credit_history),
      'purpose': constants.CreditData.PURPOSE.index(purpose),
      'amount': amount + 1,
      'savings': constants.CreditData.SAVINGS.index(savings) + 1,
      'employment_duration': constants.CreditData.EMPLOYMENT_DURATION.index(employment_duration) + 1,
      'installment_rate': constants.CreditData.INSTALLMENT_RATE.index(installment_rate) + 1,
      'personal_status_sex': constants.CreditData.PERSONAL_STATUS_SEX.index(personal_status_sex) + 1,
      'other_debtors': constants.CreditData.OTHER_DEBTORS.index(other_debtors) + 1,
      'present_residence': constants.CreditData.PRESENT_RESIDENCE.index(present_residence) + 1,
      'property': constants.CreditData.PROPERTY.index(property) + 1,
      'age': age,
      'other_installment_plans': constants.CreditData.OTHER_INSTALLMENT_PLANS.index(other_installment_plans) + 1,
      'housing': constants.CreditData.HOUSING.index(housing) + 1,
      'number_credits': constants.CreditData.NUMBER_CREDITS.index(number_credits) + 1,
      'job': constants.CreditData.JOB.index(job) + 1,
      'people_liable': constants.CreditData.PEOPLE_LIABLE.index(people_liable) + 1,
      'telephone': constants.CreditData.TELEPHONE.index(telephone) + 1,
      'foreign_worker': constants.CreditData.FOREIGN_WORKER.index(foreign_worker) + 1
    }

    st.write(credit_data)

    result = prediction(credit_data)

    # Risco de crédito
    # ruim = 0 (Aprovado)
    # bom = 1 (Reprovado)
    if result == 0:
      st.success('O crédito foi aprovado!')
    else:
      st.warning('O crédito foi reprovado!')

if __name__=='__main__':
  main()