# Gera pagina.html (publicada) a partir de fonte.html, embutindo as imagens de img/ (o app do celular não carrega os arquivos soltos).
import re, base64, pathlib
d = pathlib.Path(__file__).parent
s = (d/'fonte.html').read_text()
tipos = {'jpg':'image/jpeg','png':'image/png','svg':'image/svg+xml'}
def troca(m):
    p = d/m.group(0); return 'data:%s;base64,%s' % (tipos[p.suffix[1:]], base64.b64encode(p.read_bytes()).decode())
s = re.sub(r'img/[\w\-]+\.(?:jpg|png|svg)', troca, s)
(d/'pagina.html').write_text(s); print(len(s)//1024, 'KB')
