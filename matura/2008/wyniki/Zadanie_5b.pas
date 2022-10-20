program Zadanie_5b;

const
 szuk_dl = 12;  {Szukamy s��w tej d�ugo�ci}

var
 dane      : text;    {Plik z danymi}
 wynik1    : text;    {Plik z zaszyfrowanymi s�owami}
 wynik2    : text;    {Plik z policzonymi odpowiedziami}
 slowo     : string;  {Kolejne s�owo}
 slowo_min : string;  {Dot�d najkr�tsze s�owo}
 slowo_max : string;  {Dot�d najd�u�sze s�owo}
 dl        : integer; {D�ugo�c slowo}
 min       : integer; {D�ugo�� slowo_min}
 max       : integer; {D�ugo�� slowo_max}
 suma_dl   : integer; {Suma d�ugo�ci wszsytkich zaszyfrowanych s��w}

function odwroc(slowo: string): string;
 {Odwaca kolejno�� znak�w w slowo}
 var
  l, p   : integer; {Indeksy}
  pom    : char;    {Pomocnicza}
begin
  l     := 1;
  p     := length(slowo);
  while l < p do
   begin
    pom      := slowo[l];
    slowo[l] := slowo[p];
    slowo[p] := pom;
    l := l + 1;
    p := p - 1;
   end; {while}
  odwroc := slowo;
end; {Odwr��}

function czy_palindrom(poczatek, koniec: integer; slowo: string): boolean;
 {Sprawdza czy slowo[poczatek..koniec] jest palindromem}
 var
  odp : boolean; {Wynik funkcji}
begin
  odp := true;
  while (poczatek < koniec) and odp do
   begin
    if slowo[poczatek] <> slowo[koniec] then
      odp := false;
    poczatek := poczatek + 1;
    koniec   := koniec - 1;
   end; {while}
  czy_palindrom := odp;
end; {Czy_palindrom}

function szyfruj(slowo: string): string;
 {Szyfruje zadane s�owo}
 var
  j : integer;
begin
  j := length(slowo);
  while not czy_palindrom(1, j, slowo) do
    j := j - 1;
  szyfruj := odwroc(slowo) + copy(slowo, j+1, length(slowo)-j);
end; {Szyfruj}

begin {Program}
  assign(dane, 'slowa.txt');
  reset(dane);
  assign(wynik1, 'hasla_b.txt');
  rewrite(wynik1);
  assign(wynik2, 'slowa_b.txt');
  rewrite(wynik2);

  writeln(wynik2, '1');

  min       := MaxInt;
  max       := 0;
  slowo_min := '';
  slowo_max := '';
  suma_dl   := 0;
  while not eof(dane) do
   begin
    readln(dane, slowo);
    slowo := szyfruj(slowo);
    dl := length(slowo);
    if dl = szuk_dl then
	  writeln(wynik2, slowo);
    if dl < min then
	 begin
	  slowo_min := slowo;
	  min       := dl
	 end;
    if dl > max then
     begin
	  slowo_max := slowo;
	  max       := dl
	 end;
    suma_dl := suma_dl + dl;
    writeln(wynik1, slowo);
   end; {while}

  close(dane);
  close(wynik1);

  writeln(wynik2, '2');
  writeln(wynik2, slowo_min);
  writeln(wynik2, slowo_max);
  writeln(wynik2, '3');
  writeln(wynik2, suma_dl);

  close(wynik2);
end.
