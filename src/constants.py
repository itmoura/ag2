class CreditData():
  STATUS = ('1: Sem conta corrente','2: ... < 0 DM', '3: 0 <= ... < 200 DM', '4: ... >= 200 DM / Atribuições salariais por pelo menos 1 ano')
  CREDIT_HISTORY = ('0: Atraso no pagamento no passado', '1: Conta crítica / outros créditos em outro lugar', '2: Nenhum crédito tomado / todos os créditos pagos corretamente', '3: Créditos existentes pagos corretamente até agora', '4: Todos os créditos neste banco pagos corretamente')
  PURPOSE = ('0: Outros', '1: Carro (novo)', '2: Carro (usado)', '3: Móveis / equipamentos', '4: Rádio / TV', '5: Eletrodomésticos', '6: Reparações', '7: Educação', '8: Férias', '9: Requalificação', '10: Negócios')
  SAVINGS = ('1: Desconhecido / sem conta poupança', '2: ... < 100 DM', '3: 100 <= ... < 500 DM', '4: 500 <= ... < 1000 DM', '5: ... >= 1000 DM')
  EMPLOYMENT_DURATION = ('1: Desempregado', '2: ... < 1 ano', '3: 1 <= ... < 4 anos', '4: 4 <= ... < 7 anos', '5: ... >= 7 anos')
  INSTALLMENT_RATE = ('1: >= 35', '2: 25 <= ... < 35', '3: 20 <= ... < 25', '4: < 20')
  PERSONAL_STATUS_SEX = ('1: Masculino - divorciado / separado', '2: Feminino - não solteiro ou masculino - solteiro', '3: Masculino - casado / viúvo', '4: Feminino - solteiro')
  OTHER_DEBTORS = ('1: Nenhum', '2: Co-devedor', '3: Garantidor')
  PRESENT_RESIDENCE = ('1: < 1 ano', '2: 1 <= ... < 4 anos', '3: 4 <= ... < 7 anos', '4: >= 7 anos')
  PROPERTY = ('1: Desconhecido / sem propriedade', '2: Carro ou outro', '3: Sociedade de poupança de construção / seguro de vida', '4: Imóvel')
  OTHER_INSTALLMENT_PLANS = ('1: Banco', '2: Lojas', '3: Nenhum')
  HOUSING = ('1: De graça', '2: Aluguel', '3: Próprio')
  NUMBER_CREDITS = ('1: 1', '2: 2-3', '3: 4-5', '4: >= 6')
  JOB = ('1: Desempregado / não qualificado - não residente', '2: Não qualificado - residente', '3: Empregado qualificado / oficial', '4: Gerente / auto-empregado / empregado altamente qualificado')
  PEOPLE_LIABLE = ('1: 3 ou mais', '2: 0 a 2')
  TELEPHONE = ('1: Não', '2: Sim (sob o nome do cliente)')
  FOREIGN_WORKER = ('1: Sim', '2: Não')
  CREDIT_RISK = ('0: Ruim', '1: Bom')

class DatabaseConfig():
  HOST = 'localhost'
  USER = 'root'
  PASSWORD = 'root'
  DATABASE = 'statlog'