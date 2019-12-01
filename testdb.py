import sqls
import re

# import numpy.random as npr
# withcershit_texts = ['Ведьмак 3 — тупая гриндилка без сюжета']
# withcershit_texts_weights = [0.8, 0.2]
# print(npr.choice(withcershit_texts, 1, p=withcershit_texts_weights))
# print(npr.randint(100))

# print(sqls.witchershit_check_on_delay(1))
# sqls.witchershit_update(4)

# sqls.nintendo_update(-5)

# sqls.alive_update(6)
# print(sqls.alive_check_angry(6))
# sqls.alive_reset(6)

# test = 'Вот это новть свич обанкротилась'
# print(re.search(r'([Ss]witch)+|([Сс]ви(т)?ч)+|([Nn]intendo)+|([Нн]интендо)+', test))
# print(re.search(r'(?i)(switch|сви(т)?ч|nintendo|нинтендо)+', test))

# print(re.search(r'(?i)(witcher|ведьмак) ?!(not|не) (shit|г[ао]вно)', 'ведьмак не говно'))
print(re.search(r'(?i)^(ведьмак)([\s\-—]){1,3}(г[ао]вно)$', 'главное не говорить сане что ведьмак говно'))

# f = open("initdb.sql", "r")
# sqls.init_db(f.read())
# f.close()
