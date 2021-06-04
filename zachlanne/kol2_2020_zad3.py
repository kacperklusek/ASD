# wypełniam "piętra" wybierając zawsze element zaczynający się najwsześniej (jak jakieś elementy już są to najwsześniej
# po końcu elementu poprzednio wybranego). powtarzam dopóki mogę wybrać jakiś klocek.
# uzasadnienie poprawności:
# jeśli nie wybiorę elementu x zaczynającego się najwcześniej, dla i-tego piętra, to mogą zdarzyć się dwa przypadki:
#   1) piętro i+1 zaczyna się za końcem elementu x, wtedy mogę go wybrać w każdej następnej iteracji, i będzie on na
#      piętrze i-tym, czyli skończymy z układem równoważnym, wybraniu elementu x dla i-tego piętra
#   2) piętro i+1 zaczyna się w środku elementu x, wtedy nigdy później nie mogę go wybrać, bo będzie "zwisał" po lewej
#      stronie
# wniosek: zawsze trzeba wybierać najwcześniej zaczynające się kawałki, tak jak opisałem to wyżej


