program Zadanie_5a;

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


procedure odwroc(var slowo: string);
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
end; {Odwr��}

begin
  assign(dane, 'slowa.txt');
  reset(dane);
  assign(wynik1, 'hasla_a.txt');
  rewrite(wynik1);
  assign(wynik2, 'slowa_a.txt');
  rewrite(wynik2);

  min := MaxInt; 
  max := 0;
  while not eof(dane) do
   begin
    readln(dane, slowo);
    odwroc(slowo);
    dl := length(slowo);
    if dl < min then
     begin 
      slowo_min := slowo; 
      min       := dl; 
     end;
    if dl > max then 
     begin 
      slowo_max := slowo; 
      max       := dl; 
     end;
    writeln(wynik1, slowo);
   end; {while}

  close(dane);
  writeln(wynik2, slowo_min, ' ',min);
  writeln(wynik2, slowo_max, ' ',max);
  close(wynik1);
  close(wynik2)
end.
