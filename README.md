# PAINT - dokumentacja projektu

Link do strony: https://fotoreporterzy-paint.netlify.app/

## Temat

Aplikacja webowa do obsługi studia fotograficznego

## Zespół

- Krzysztof Fijałkowski - kierownik projektu/programista back-end
- Bartłomiej Pełka - programista back-end/dev-ops
- Rafał Szczepaniak - programista dev-ops/programista back-end
- Adam Jeliński - programista front-end

## Wymagania

### Funkcjonalne

- możliwość sprawdzenia terminów
- oferta, opisy pracowników, opisy samego studia, informacje
- Formularz kontaktowy
- możliwość odbioru prac (zabezpieczone hasłem odbitki lub zip odbitek)
- widok administratora (fotografa) z możliwością min. dodania nowych zdjęć, sprawdzenia czy zdjęcia zostały odebrane itp

### Niefunkcjonalne

- konteneryzacja - Docker compose

## Założenia architektoniczne aplikacji

W założeniu aplikacja ma 3 moduły:
- Frontend - zdeployowany na Netlify, frontend napisany w vue + vite + vuetify + pinia jest zdeployowany na Netlify dzięki czemu mamy działający produkt gotowy do użytku
- Serwer plików - Ubuntu serwer (pliki relatywnie rzadko czytane ~parę razy dziennie)
- Baza danych - Supabase (duża dostępność, łatwe stawianie)

### Schemat:
![image](https://hackmd.io/_uploads/rJtBRCEH0.png)


## Opis wykorzystania narzędzi programowych w powiązaniu z ww założeniami funkcjonalnymi i architektonicznymi

- **Supabase** - Supabase, jest to baza na technologi postgres, jest to dobre rozwiązanie ze względu na ilość wbufowanych narzędzi jak autoryzacja użytkowników czy RLS
- **Ubuntu server** - serwer trzymający zdjęcia, jest to własny serwer (komputer z zainstalowanym ubuntu serwer) Ze względu na reużycie nie używanego sprzętu i dostanie serwera plików o dość dużym rozmiarze za darmo, wiedząc, że zdjęcia są duże i nie potrzebna jest dostępność na poziomie > 99% ani nie jest potrzebna duża wydajność ponieważ nie występuje sytuacja aby zdjęcia pobierane były częściej niż ~2 razy dziennie. Dlatego też, jest to optymalne rozwiązanie
- **vue** - framework JavaScript, który umożliwia budowanie interfejsów użytkownika oraz aplikacji SPA
- **netlify** - platforma do deployowania aplikacji webowych umożliwiająca bardzo szybką i łatwą deployowanie ze względu na min. połączenie z github.

## Opis realizacji projektu (wykonane czynności, napotkane problemy itd)

Wszystko zostało zrobione w dokładnie dwie doby

### Realizacja:
1. **Stworzenie prototypu w Figma** - rozpoczęliśmy od wizualizacji podstron i modelu aplikacji co zrobiliśmy za pomocą Figmy, jest ten plik w dokumentacji w repozytorium w formie pdf
2. **Postawienie Netlify** - należało połączyć netlify z github aby był tworzony deployment
3. **Realizacja frontend** - należało napisać frontend
4. **Zaprojektowanie ER bazy danych** - za pomocą draw.io zaprojektowaliśmy model ER, z którego zrobiliśmy create_db.sql
5. **Postawienie Supabase** - Stworzyliśmy projekt na supabase i wgraliśmy na niego create_db.sql, dodaliśmy w supabase użytkownika - admina oraz według instrukcji supabase zaimplementowaliśmy logowanie oraz używanie bazy
6. **Postawienie serwera plików** - Postawitne własnego serwera plików było czynnością niespodziewanie skomplikowaną z wielu powodów.Niektóre opisane poniżej, ostatecznie na serwerze zostało uruchomione fastapi wspierające TLS. 


### Problemy

Co do problemów trzeba napomnieć dlaczego w ogóle TLS?
Serwis na Netlify korzysta z HTTPS i aby móc się z niego łączyć do jakiegokolwiek serwera również musimy używać HTTPS-a, nie możliwym było wyłączenie HTTPS na Netlify

1. **TLS** - W trakcie stawiania serweru backendowego w punkcie w którym z testowego http przechodziliśmy na docelowe połączenie po https z backendem napotkaliśmy wiele problemów. Początkowo serwer backend miał być obsługiwany przez nginx, lecz wykorzystane narzędzie automatycznie aktualizujące konfigurację nginxa Letsencrypt generowało konfigurację która nie chciała działać. Po wielu próbach zdecydowaliśmy że spróbujemy użyć zamiast tego Apache'a, lecz tam napotkaliśmy ten sam problem. Ostatecznie rozwiązaliśmy problem implementując własny prosty serwer plików używając FastAPI i uruchamiając go za pomocą Uvicorna. Tam też napotkaliśmy drobny problem dotyczący daemona odmawiającego czytania certyfikatów z plików konfiguracyjnych ale udało się go rozwiązać.
2. **LTE router port forwarding** - Pierwotnie plan polegał na podłączeniu komputera do routera LTE i po skonfigurowaniu port forwarding w taki sposób używania serwera plików. Okazało się to nie możliwe bo port forwarding był blokowany przez dostawcę usług.
3. **Statyczne IP** - aby mieć serwer który mimo bycia resetowanym itp miał nadal statyczne IP poza konfiguracją routera potrzebne było również używanie No-Ip
4. **TLS z No-IP** - Okazuje się, że darmowa wersja No-IP nie wspiera TLS-a więc musieliśmy przetestować wersję rozbudowaną
5. **SPA na Netlify** - Netlify domyślnie nie wspierało SPA (single page application) i trzeba to było skonfigurować
6. **Wydajność Dockera** - Docker okazał się zużywać bardzo dużo zasobów na ograniczonym serwrze, więc ze względu na słabe podzespoły wykorzystanego serwera zrezygnowaliśmy z dodatkowej konteneryzacji elementów gdyż konfiguracja nie pozwalała nam na uruchomienie kilku kontenerów (oczywiście teoretycznie byłoby to możliwe i wygodniejsze w deployowaniu).
7. **CORS** - aby móc łączyć się z front-endu do serwera plików należało skonfigurować CORS
8. i wiele więcej...


## Opis modułów

### Supabase
Do Supabase można łączyć się używając Supabase client-a którego definiujemy podając mu url projektu i anon key. Używając Supabase klienta bezpośrednio z Front-end-u jesteśmy w stanie w bezpieczny i wydajny sposób czytać i dodawać tabele z bazy danych.

Dokumentacja Supabase: https://supabase.com/docs/reference/javascript/introduction

### Serwer plików
Ostatecznie jest to serwer napisany w python FastApi, udostępniający następujące api:

#### Endpoint: `/files/{file_path:path}`

##### Przykład użycia:
```bash
curl -X GET "http://127.0.0.1:8000/files/somefile.txt"
```

##### Opis endpointu:
Ten endpoint umożliwia pobranie pliku z serwera na podstawie podanej ścieżki do pliku. Klient wysyła żądanie GET na ten endpoint, podając ścieżkę do pliku jako parametr. Jeśli plik istnieje, serwer zwraca go jako odpowiedź. W przeciwnym razie, serwer zwraca błąd 404 z informacją, że plik nie został znaleziony.

#### Endpoint: `/upload`

##### Przykład użycia:
```bash
curl -X POST "http://127.0.0.1:8000/upload" -F "file=@/path/to/your/file.zip" -F "secretKey=your_secret_key"
```

##### Opis endpointu:
Ten endpoint umożliwia przesyłanie plików ZIP na serwer. Klient wysyła żądanie POST zawierające plik ZIP oraz sekretne hasło (secretKey). Serwer weryfikuje sekretne hasło i sprawdza, czy przesłany plik ma rozszerzenie `.zip`. Jeśli weryfikacja się powiedzie, serwer zapisuje plik w unikalnym folderze, a następnie rozpakowuje jego zawartość. W przypadku powodzenia zwracany jest unikalny identyfikator UUID folderu. Jeśli weryfikacja się nie powiedzie lub plik nie jest poprawnym plikiem ZIP, zwracany jest odpowiedni kod błędu i komunikat.

#### Endpoint: `/getFileList/{folder_path:path}`

##### Przykład użycia:
```bash
curl -X GET "http://127.0.0.1:8000/getFileList/somefolder"
```

##### Opis endpointu:
Ten endpoint zwraca listę plików znajdujących się w podanym folderze. Klient wysyła żądanie GET na ten endpoint, podając ścieżkę do folderu jako parametr. Serwer sprawdza, czy folder istnieje i czy jest faktycznie folderem. Jeśli tak, zwracana jest lista plików znajdujących się w tym folderze. W przeciwnym razie serwer zwraca odpowiedni kod błędu i komunikat, informując, że folder nie został znaleziony lub ścieżka jest niepoprawna.

link do dokumentacji swagger: https://fotorepofileserver.ddns.net:8000/docs

### Frontend:
- Strona główna
- Panel logowania
- Panel do przeglądania i pobierania odbitek
- Panel administratora (dodawanie nowych zdjęć, przeglądanie statusu albumów)
- Panel do rezerwacji terminów (kalendarz)

### Technologie
- Python FastApi
- Ubuntu server
- Vue.js
- github
- REST
- Supabase
- Netlify

## Instrukcja instalacji produktu
Wymagane paczki:
- frontend
    - pnpm
- backend
    - python3, pip
    - fastapi (pip)
    - uvicorn (pip)

Aby na własnym serwerze zainstalować nasz produkt należy zapewnić następujące rzeczy:
1. Sklonować lokalnie repozytorium github
2. Stworzyć własny serwer plików za pomocą fastapi. Aplikację fastapi należy uruchomić komendą (z poziomu repozytorium)
```bash=
python3 file-server/script.py
```
3. Utworzyć projekt na supabase i odpowiednie klucze dodać.
4. W celu zbudowania frontendu należy wykonać następujące komendy (z poziomu repozytorium) co wygeneruje pliki gotowe do wrzucenia na dowolny serwer WWW
```bash=
cd frontend && pnpm install && pnpm run build 
```
5. Skonfigurować w Netlify deployment aplikacji, ustawiając wcześniej odpowiednie forwardy portów oraz konfigurację firewall

## Instrukcja obsługi produktu

### Zwykły użytkownik
Użytkownik korzystający z naszej aplikacji ma kilka podstron w aplikacji webowej, są to
- [strona startowa](https://fotoreporterzy-paint.netlify.app/), na której może zobaczyć krótki opis studia i skład zespołu
    ![image](https://hackmd.io/_uploads/S18QPyBHA.png)
- [podstrona ze zdjęciami](https://fotoreporterzy-paint.netlify.app/offer) przykładowymi, prezentująca ofertę studia
    ![image](https://hackmd.io/_uploads/HJJHP1HHA.png)
- [podstrona na której można odebrać zamówione zdjęcia](https://fotoreporterzy-paint.netlify.app/photos) - w tym celu należy podać kod dostępu do zdjęć
    ![image](https://hackmd.io/_uploads/rkzUwJBrA.png)
    Po podaniu kodu wyświetlone zostaną zdjęcia a pod nimi znajdować się będzie przycisk który umożliwia ich pobranie
    ![image](https://hackmd.io/_uploads/H1cZPJrH0.png)
- [podstrona z kalendarzem](https://fotoreporterzy-paint.netlify.app/check-slot) na której można sprawdzić wolne terminy
    ![image](https://hackmd.io/_uploads/SkiFPkBrC.png)
- [podstrona kontaktowa](https://fotoreporterzy-paint.netlify.app/contact) na której można wysłać wiadomość do studia, przesłane wiadomości widoczne są potem w panelu administratora
    ![image](https://hackmd.io/_uploads/r1zaD1rS0.png)
    Pomyślne przesłanie wiadomości potwierdzi komunikat.
### Administrator
Administrator - fotograf ma kilka podstron, najpierw musi się zalogować na:
- [strona logowania](https://fotoreporterzy-paint.netlify.app/admin)
![image](https://hackmd.io/_uploads/HyXSTkHSR.png)
- [strona wiadomości](https://fotoreporterzy-paint.netlify.app/admin/messages) gdzie znajdują się wszystkie wiadomości wysłane do fotografa, po przeczytaniu może on je usuwać:
![image](https://hackmd.io/_uploads/H1rnAySB0.png)

- [dodanie sesji](https://fotoreporterzy-paint.netlify.app/admin/upload) gdzie może on wstawić nową sesję:
![image](https://hackmd.io/_uploads/HJljRyBS0.png)

- [utworzenie terminów działania studia](https://fotoreporterzy-paint.netlify.app/admin/slots) gdzie może on dodać w jakich terminach działa studio!![image](https://hackmd.io/_uploads/HJAYAyHS0.png)
