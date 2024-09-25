import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Определяем диапазоны для критериев
loading_speed = ctrl.Antecedent(np.arange(0, 11, 1), 'loading_speed')
design = ctrl.Antecedent(np.arange(0, 11, 1), 'design')
security = ctrl.Antecedent(np.arange(0, 11, 1), 'security')
usability = ctrl.Antecedent(np.arange(0, 11, 1), 'usability')
quality = ctrl.Consequent(np.arange(0, 11, 1), 'quality')

# 2. Определение функций принадлежности (низкий, средний, высокий)
loading_speed.automf(3)
design.automf(3)
security.automf(3)
usability.automf(3)
quality.automf(3)

# 3. Простые правила для Fuzzy MCDM
rule1 = ctrl.Rule(loading_speed['good'] & design['good'] & security['good'] & usability['good'], quality['good'])
rule2 = ctrl.Rule(loading_speed['average'] & design['average'] & security['average'] & usability['average'], quality['average'])
rule3 = ctrl.Rule(loading_speed['poor'] & design['poor'] & security['poor'] & usability['poor'], quality['poor'])

# 4. Создание системы управления и симуляция
quality_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
quality_sim = ctrl.ControlSystemSimulation(quality_ctrl)

# 5. Вводим данные (вручную для первой итерации)

quality_sim.input['loading_speed'] = int(input("loading_speed from 1 to 10? "))
quality_sim.input['design'] = int(input("design from 1 to 10? "))
quality_sim.input['security'] = int(input("security from 1 to 10? "))
quality_sim.input['usability'] = int(input("usability from 1 to 10? "))
#quality_sim.input['loading_speed'] = 7  # Например, 7 из 10
#quality_sim.input['design'] = 6         # Оценка дизайна
#quality_sim.input['security'] = 8       # Оценка безопасности
#quality_sim.input['usability'] = 5      # Оценка удобства использования

# 6. Запуск симуляции и вывод результата
quality_sim.compute()
print(f"Итоговая оценка качества: {quality_sim.output['quality']}")
