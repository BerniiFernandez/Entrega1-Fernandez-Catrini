from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Vista de inicio

def home(request):
    return render(request, "home.html")

def sobrenosotros(request):
    return render(request, "sobreNosotros.html")

def netflix(request):
    serienetflix1 = Netflix(title="Stranger Things", photo='/media/images/stranger-things-img.jpeg', date=date(2022, 9, 28), author="Bernardita Fernández", qualification=8.7, body="Cuando un niño desaparece, sus amigos, la familia y la policía se ven envueltos en una serie de eventos misteriosos al tratar de encontrarlo. Su ausencia coincide con el avistamiento de una criatura terrorífica y la aparición de una extraña niña.")
    serienetflix2 = Netflix(title="Better Call Saul", photo="/media/images/better-call-saul-img.jpeg", date=date(2022, 9, 28), author="Bernardita Fernández", qualification=8.9, body="Es una serie de televisión estadounidense creada por Vince Gilligan y Peter Gould. Se trata de una precuela de breaking Bad. La acción se ubica en en años 2002 en torno al abogado James McGrill seis años antes de su aparición en breaking bad.")
    serienetflix3 = Netflix(title="Peaky Blinders", photo="/media/images/peaky-blinders-img.jpeg", date=date(2022, 9, 29), author="Bernardita Fernández", qualification=8.8, body="Gran Bretaña vive la posguerra. Los soldados regresan, se acuñan nuevas revoluciones y nacen bandas criminales en una nación agitada. En Birmingham, una pandilla de gangsters callejeros asciende hasta convertirse en los reyes de la clase obrera.")
    serienetflix4 = Netflix(title="Ozark", photo="/media/images/ozark-img.jpeg", date=date(2022, 9, 29), author="Bernardita Fernández", qualification=8.5, body="Una financista traslada a su familia a Ozarks. Después de que un Olán de lavado de dinero va mal, se ve obligado a pagar una deuda a un narcotraficante mexicano para mantener a su familia.")
    serienetflix1.save()
    serienetflix2.save()
    serienetflix3.save()
    serienetflix4.save()
    seriesnetflix = [serienetflix1, serienetflix2, serienetflix3, serienetflix4]
    return render(request, "netflix.html", {'seriesnetflix':seriesnetflix})

def primevideo(request):
    serieprime1 = Prime(title="The Terminal List", photo="/media/images/the-terminal-list-img.jpeg", date=date(2022, 9, 30), author="Bernardita Fernández", qualification=8, body="James Reece regresa a casa después de que todo su pelotón de Navy SEAL es emboscado, solo para descubrir qué nuevas fuerzas oscuras trabajan en su contra y ponen en peligro a sus seres queridos.")
    serieprime2 = Prime(title="The Lord of the Rings: The Rings of Power", photo="/media/images/the-rings-of-power-img.jpeg", date=date(2022, 9, 30), author="Bernardita Fernández", qualification=6.7, body="Situada en el universo del Señor de los Anillos, la historia trata sobre Galadriel, una elfa del clan Noldor, quien se enfrentará junto a otros guerreros al temido resurgimiento del mal en la tierra media, los cuales forjarán legados que perdurarán mucho tiempo después de su desaparición.")
    serieprime3 = Prime(title="The Boys", photo="/media/images/the-boys-img.jpeg", date=date(2022, 9, 30), author="Bernardita Fernández", qualification=8.7, body="Cuando los superhéroes abusan de sus superpoderes en lugar de usarlos para el bien, unos “muchachos” se embarcan en una búsqueda heroica para exponer sus secretos.")
    serieprime4 = Prime(title="This Is Us", photo="/media/images/this-is-us-img.jpeg", date=date(2022, 9, 30), author="Bernardita Fernández", qualification=8.7, body="La historia de la familia Pearson comienza en 1979, cuando los trillizos de Jack y Rebecca llegan a la familia de una manera inesperada. Una saga emotiva sobre el amor, la vida y la derrota que se desenvuelve durante varias generaciones.")
    serieprime1.save()
    serieprime2.save()
    serieprime3.save()
    serieprime4.save()
    seriesprime = [serieprime1, serieprime2, serieprime3, serieprime4]
    return render(request, "primevideo.html", {'seriesprime':seriesprime})

def hbomax(request):
    seriehbo1 = HBO(title="House of the Dragon", photo="/media/images/house-of-the-dragon-img.jpeg", date=date(2022, 10, 2), author="Brian Catrini", qualification=8.8, body="Basada en el libro Fuego y Sangre de George R. R. Martín y dirigida entre otros por Miguel Sapochnik, responsable de los capítulos más emblemáticos de Games of Thrones, La Casa del Dragón (en inglés House of the Dragon) es una serie de fantasía cuya historia se desarrolla 200 años antes de los acontecimientos narrados en Games of Thrones. Viserys Targaryen, interpretado por Paddy Considine es el rey de Poniente y debe elegir un sucesor para el Trono de Hierro. Su esposa Aemma está embarazada y Viserys espera ansioso el nacimiento de un heredero varón, pero durante el parto Aemma y el niño mueren. Entonces, por consejo de la Mano del Rey, y a pesar de la ferviente oposición de su hermano Daemon (Matt Smith), nombra a su única hija viva Rhaenyra (Emma D’Arcy) como su sucesora. A partir de allí y a lo largo de los años se intensificarán los conflictos con el resto de los aspirantes al trono, principalmente los de la Casas Velaryon y Hightower, quienes no dudarán en promover batallas, asesinatos, traiciones  y hasta uniones insestuosas para lograr su objetivo.")
    seriehbo2 = HBO(title="Succesion", photo="/media/images/succesion-img.jpeg", date=date(2022, 10, 2), author="Brian Catrini", qualification=8.8, body="Esta comedia dramática creada por Jesse Armstrong, cuenta la vida de una poderosa y adinerada familia, dueña de un imperio de empresas de entretenimiento y medios audiovisuales. Logan Roy, interpretado por Brian Cox, es el patriarca de la familia, más interesado en el dinero y el poder que en su propio entorno. Su reemplazante natural al frente del enorme negocio familiar es su hijo Kendall (Jeremy Strong), quien ve frustrarse todas sus ambiciones cuando Logan decide seguir un tiempo más al frente del conglomerado. Es en ese momento que comienza una lucha por el poder a la que se suman los otros tres hijos de Logan: Connor (Alan Ruck), el mayor, Román (Kieran Culkin), el menor de los hermanos, y Shiv (Sarah Snook), la única mujer. Será una competencia en la que habrá de todo: intrigas, traiciones y golpes bajos, todo bajo la atenta mirada de Logan que no duda en poner a sus herederos unos contra otros para su conveniencia y beneficio.")
    seriehbo3 = HBO(title="The Flight Attendant", photo="/media/images/the-flight-attendant-img.jpeg", date=date(2022, 10, 2), author="Brian Catrini", qualification=7.1, body="En esta comedia de humor negro, basada en la novela de Chris Bohjalian, Kaley Cuoco interpreta a Cassie Bowden, una azafata que en su tiempo libre lleva una vida bastante alocada, plagada de fiestas y exceso de alcohol. Durante un vuelo conoce a Alex Sokolov (Michiel Huisman), quien luego de compartir con ella una noche de borrachera en Bangkok, aparece asesinado a su lado en la cama de un hotel. Cassie, que no recuerda nada, abandona el hotel y al día siguiente se embarca en un vuelo a Nueva York como si nada hubiera sucedido. Una vez allí, es interrogada por el FBI sobre su estadía en Bangkok, por lo que debe intentar recordar qué fue lo que sucedió y si es posible que ella haya asesinado a Alex.")
    seriehbo4 = HBO(title="The Sopranos", photo="/media/images/the-sopranos.jpeg", date=date(2022, 10, 2), author="Brian Catrini", qualification=9.2, body="Esta serie creada por David Chase, narra la vida de Tony Soprano (James Gandolfini), integrante de una familia mafiosa de Nueva Jersey, quien debe lidiar con los problemas derivados de su actividad delictiva que ponen en riesgo constante su seguridad y la de la organización que lidera, así como también la de su propia familia integrada por Carmela, su esposa, papel interpretó por Edie Falco, sus hijos Anthony Jr. (Robert Iller) y Meadow (Jamie-Lynn Sigler), su madre Livia (Nancy Marchand) y Christopher Moltisanti (Michael Imperioli) sobrino y protegido de Tony. Las constantes amenazas y traiciones a las que se ve sometido, el tratar de mantener a sus hijos alejados de los rumores sobre su forma de ganarse la vida, y la relación paralela a su matrimonio que mantiene con una joven rusa, provocan que Tony comience a sufrir ataques de pánico, lo que lo lleva a consultar a la Dra. Melfi (Lorraine Bracco), psiquiatra a quien Tony le revela detalles sobre su infancia, la relación con su padre también mafioso y su manipuladora y vengativa madre, los problemas con su esposa Carmela, y los sentimientos respecto a sus lazos con la mafia. La confianza entre Tony y su terapeuta va creciendo con el tiempo y empieza a desarrollarse un vínculo entre ambos más allá de lo profesional.")
    seriehbo1.save()
    seriehbo2.save()
    seriehbo3.save()
    seriehbo4.save()
    serieshbo = [seriehbo1, seriehbo2, seriehbo3, seriehbo4]
    return render(request, "hbomax.html", {'serieshbo':serieshbo})

def disneyplus(request):
    seriedisney1 = Disney(title="She-Hulk: Attorney at Law", photo="/media/images/she-hulk-img.jpeg", date=date(2022, 10, 4), author="Brian Catrini", qualification=5.1, body="Jennifer Walters es una abogada de 30 años que busca triunfar en su carrera. Tras verse involucrada en un accidente automovilístico junto a su primo, el doctor Bruce Banner, descubre que posee los poderes de Hulk. Ahora deberá encontrar un equilibrio entre su profesión, su vida amorosa y el ser una superhéroe.")
    seriedisney2 = Disney(title="Moon Knight", photo="/media/images/moon-knight-img.jpeg", date=date(2022, 10, 4), author="Brian Catrini", qualification=7.3, body="Steven Brant, el empleado de un museo, descubre que tiene un trastorno de identidad disociativo y por esto debe compartir su cuerpo con Marc Spector, un mercenario que obtiene poderes de Khonshu, el Dios egipcio de la Luna, para luchar contra el mal. Steven deberá lidiar con sus múltiples personalidades mientras se encuentra inmerso en una batalla mortal entre los Dioses de Egipto.")
    seriedisney3 = Disney(title="Ms. Marvel", photo="/media/images/ms-marvel-img.jpeg", date=date(2022, 10, 4), author="Brian Catrini", qualification=6.2, body="La vida de la joven de 16 años Kamala Khan, fanática de los superhéroes, cambia radicalmente cuando encuentra un brazalete capaz de proyectar una gran energía cósmica. Kamala debe aprender a utilizar sus nuevos poderes para hacer el bien, al igual que los héroes que tanto admira, y evitar que el brazalete ponga en peligro a toda la humanidad.")
    seriedisney4 = Disney(title="Obi-Wan Kenobi", photo="/media/images/obi-wan-kenobi-img.jpeg", date=date(2022, 10, 4), author="Brian Catrini", qualification=7.1, body="Diez años después de la terrible Orden 66 por la cual todos los caballeros Jedi debían ser eliminados, la galaxia se encuentra gobernada por el Imperio, liderado por el Canciller Palpatine. Obi-Wan deberá sobrevivir al régimen Sith mientras se enfrenta a los eventos pasados acontecidos entre él y Darth Vader, su ex aprendiz y mejor amigo quien, ahora como segundo al mando del Canciller, lo busca para asesinarlo.")
    seriedisney1.save()
    seriedisney2.save()
    seriedisney3.save()
    seriedisney4.save()
    seriesdisney = [seriedisney1, seriedisney2, seriedisney3, seriedisney4]
    return render(request, "disneyplus.html", {'seriesdisney':seriesdisney})

def detallenetflix(request, id):
    detail = Netflix.objects.get(id=id)
    return render(request, "detalleNetflix.html", {'detail':detail})

def detalleprime(request, id):
    detail = Prime.objects.get(id=id)
    return render(request, "detallePrime.html", {'detail':detail})

def detallehbo(request, id):
    detail = HBO.objects.get(id=id)
    return render(request, "detalleHBO.html", {'detail':detail})

def detalledisney(request, id):
    detail = Disney.objects.get(id=id)
    return render(request, "detalleDisney.html", {'detail':detail})




# CRUD

@login_required
def listanetflix(request):
    listadonetflix = Netflix.objects.all()
    return render(request, "listaNetflix.html", {'listadonetflix':listadonetflix})

@login_required
def listaprime(request):
    listadoprime = Prime.objects.all()
    return render(request, "listaPrime.html", {'listadoprime':listadoprime})

@login_required
def listahbo(request):
    listadohbo = HBO.objects.all()
    return render(request, "listaHBO.html", {'listadohbo':listadohbo})

@login_required
def listadisney(request):
    listadodisney = Disney.objects.all()
    return render(request, "listaDisney.html", {'listadodisney':listadodisney})

def netflixform(request):
    if request.method == "POST":
        form = NetflixForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            photo = informacion["photo"]
            date = informacion["date"]
            author = informacion["author"]
            qualification = informacion["qualification"]
            body = informacion["body"]
            netflix = Netflix(title=title, photo=photo, date=date, author=author, qualification=qualification, body=body)
            netflix.save()
            listadonetflix = Netflix.objects.all()
            return render(request, "listaNetflix.html", {'listadonetflix':listadonetflix})

    else:
        formulario = NetflixForm()
        return render(request, "netflixForm.html", {'formulario':formulario})


def primeform(request):
    if request.method == "POST":
        form = PrimeForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            photo = informacion["photo"]
            date = informacion["date"]
            author = informacion["author"]
            qualification = informacion["qualification"]
            body = informacion["body"]
            prime = Prime(title=title, photo=photo, date=date, author=author, qualification=qualification, body=body)
            prime.save()
            listadoprime = Prime.objects.all()
            return render(request, "listaPrime.html", {'listadoprime':listadoprime})

    else:
        formulario = PrimeForm()
        return render(request, "primeForm.html", {'formulario':formulario})
        
def hboform(request):
    if request.method == "POST":
        form = HBOForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            photo = informacion["photo"]
            date = informacion["date"]
            author = informacion["author"]
            qualification = informacion["qualification"]
            body = informacion["body"]
            hbo = HBO(title=title, photo=photo, date=date, author=author, qualification=qualification, body=body)
            hbo.save()
            listadohbo = HBO.objects.all()
            return render(request, "listaHBO.html", {'listadohbo':listadohbo})

    else:
        formulario = HBOForm()
        return render(request, "hboForm.html", {'formulario':formulario})

def disneyform(request):
    if request.method == "POST":
        form = DisneyForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            photo = informacion["photo"]
            date = informacion["date"]
            author = informacion["author"]
            qualification = informacion["qualification"]
            body = informacion["body"]
            disney = Disney(title=title, photo=photo, date=date, author=author, qualification=qualification, body=body)
            disney.save()
            listadodisney = Disney.objects.all()
            return render(request, "listaDisney.html", {'listadodisney':listadodisney})

    else:
        formulario = DisneyForm()
        return render(request, "disneyForm.html", {'formulario':formulario})


def editarserienetflix(request, id):
    netflix = Netflix.objects.get(id=id)
    if request.method == "POST":
        form = NetflixForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            netflix.title = informacion["title"]
            netflix.photo = informacion["photo"]
            netflix.date = informacion["date"]
            netflix.author = informacion["author"]
            netflix.qualification = informacion["qualification"]
            netflix.body = informacion["body"]
            netflix.save()
            listadonetflix = Netflix.objects.all()
            return render(request, "listaNetflix.html", {'listadonetflix':listadonetflix})

    else:
        formulario = NetflixForm(initial={'title': netflix.title, 'photo': netflix.photo, 'date': netflix.date, 'author': netflix.author, 'qualification': netflix.qualification, 'body': netflix.body})
        return render(request, "editarSerieNetflix.html", {'formulario':formulario, 'netflix':netflix})

def editarserieprime(request, id):
    prime = Prime.objects.get(id=id)
    if request.method == "POST":
        form = PrimeForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            prime.title = informacion["title"]
            prime.photo = informacion["photo"]
            prime.date = informacion["date"]
            prime.author = informacion["author"]
            prime.qualification = informacion["qualification"]
            prime.body = informacion["body"]
            prime.save()
            listadoprime = Prime.objects.all()
            return render(request, "listaPrime.html", {'listadoprime':listadoprime})

    else:
        formulario = PrimeForm(initial={'title': prime.title, 'photo': prime.photo, 'date': prime.date, 'author': prime.author, 'qualification': prime.qualification, 'body': prime.body})
        return render(request, "editarSeriePrime.html", {'formulario':formulario, 'prime':prime})

def editarseriehbo(request, id):
    hbo = HBO.objects.get(id=id)
    if request.method == "POST":
        form = HBOForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            hbo.title = informacion["title"]
            hbo.photo = informacion["photo"]
            hbo.date = informacion["date"]
            hbo.author = informacion["author"]
            hbo.qualification = informacion["qualification"]
            hbo.body = informacion["body"]
            hbo.save()
            listadohbo = HBO.objects.all()
            return render(request, "listaHBO.html", {'listadohbo':listadohbo})

    else:
        formulario = HBOForm(initial={'title': hbo.title, 'photo': hbo.photo, 'date': hbo.date, 'author': hbo.author, 'qualification': hbo.qualification, 'body': hbo.body})
        return render(request, "editarSerieHBO.html", {'formulario':formulario, 'hbo':hbo})

def editarseriedisney(request, id):
    disney = Disney.objects.get(id=id)
    if request.method == "POST":
        form = DisneyForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            disney.title = informacion["title"]
            disney.photo = informacion["photo"]
            disney.date = informacion["date"]
            disney.author = informacion["author"]
            disney.qualification = informacion["qualification"]
            disney.body = informacion["body"]
            disney.save()
            listadodisney = Disney.objects.all()
            return render(request, "listaDisney.html", {'listadodisney':listadodisney})

    else:
        formulario = DisneyForm(initial={'title': disney.title, 'photo': disney.photo, 'date': disney.date, 'author': disney.author, 'qualification': disney.qualification, 'body': disney.body})
        return render(request, "editarSerieDisney.html", {'formulario':formulario, 'disney':disney})


def eliminarserienetflix(request, id):
    netflix = Netflix.objects.get(id=id)
    netflix.delete()
    listadonetflix = Netflix.objects.all()
    return render(request, "listaNetflix.html", {'listadonetflix':listadonetflix})

def eliminarserieprime(request, id):
    prime = Prime.objects.get(id=id)
    prime.delete()
    listadoprime = Prime.objects.all()
    return render(request, "listaPrime.html", {'listadoprime':listadoprime})

def eliminarseriehbo(request, id):
    hbo = HBO.objects.get(id=id)
    hbo.delete()
    listadohbo = HBO.objects.all()
    return render(request, "listaHBO.html", {'listadohbo':listadohbo})

def eliminarseriedisney(request, id):
    disney = Disney.objects.get(id=id)
    disney.delete()
    listadodisney = Disney.objects.all()
    return render(request, "listaDisney.html", {'listadodisney':listadodisney})




# Vistas de búsqueda

def busquedanetflix(request):
    return render(request, "busquedaNetflix.html")

def buscarserienetflix(request):
    if request.GET["title"]:
        title = request.GET["title"]
        netflixseries = Netflix.objects.filter(title__icontains = title)
        return render(request, "resultadoNetflix.html", {'netflixseries': netflixseries, 'title': title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)

def busquedaprime(request):
    return render(request, "busquedaPrime.html")

def buscarserieprime(request):
    if request.GET["title"]:
        title = request.GET["title"]
        primeseries = Prime.objects.filter(title__icontains = title)
        return render(request, "resultadoPrime.html", {'primeseries': primeseries, 'title': title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)

def busquedahbo(request):
    return render(request, "busquedaHBO.html")

def buscarseriehbo(request):
    if request.GET["title"]:
        title = request.GET["title"]
        hboseries = HBO.objects.filter(title__icontains = title)
        return render(request, "resultadoHBO.html", {'hboseries': hboseries, 'title': title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)

def busquedadisney(request):
    return render(request, "busquedaDisney.html")

def buscarseriedisney(request):
    if request.GET["title"]:
        title = request.GET["title"]
        disneyseries = Disney.objects.filter(title__icontains = title)
        return render(request, "resultadoDisney.html", {'disneyseries': disneyseries, 'title': title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)





# Formulario de usuarios 

def loginapp(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST["username"]
            password=request.POST["password"]
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "home.html", {'message':f"Bienvenido {user}"})
            else:
                return render(request, "loginapp.html", {'formulario':form, 'mensaje':"Usuario o contraseña incorrectos"})
        else:
            return render(request, "loginapp.html", {'formulario':form, "mensaje":"Usuario o contraseña incorrectos"})

    else:
        form=AuthenticationForm()
        return render(request, "loginapp.html", {"formulario":form})


def registerapp(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "home.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registerapp.html", {"formulario":form, "mensaje":"Formulario inválido"})

    else:
        form=UserRegisterForm()
        return render(request, "registerapp.html", {"formulario":form})



@login_required
def perfil(request):
    usuario = request.user
    return render(request, "perfil.html", {"usuario": usuario})

@login_required
def editarperfil(request):
    usuario = request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.email = informacion["email"]
            usuario.link = informacion["link"]
            usuario.photo = informacion["photo"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.save()
            return render(request, "perfil.html")
        else:
            return render(request, "editarperfil.html", {"formulario":form, "usuario":usuario, "mensaje":"Formulario inválido"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, "editarperfil.html", {"formulario":form, "usuario":usuario})

