program Wybory;

const
 l_okr = 20;  {Liczba okr�g�w}
 l_kom = 6;   {Liczba komitet�w}

 var
  wyn        : text;                                 {Plik z wynikami}
  glosy      : array[1..l_okr,1..l_kom] of integer;  {Liczby g�os�w oddanych w poszczeg�lnych okr�gach}
  l_mandatow : array[1..l_okr] of integer;           {Liczby mandat�w do rodzielenia w poszczeg�lnych okr�gach} 
  mandat     : array[1..l_okr,1..l_kom] of integer;  {Liczby mandat�w przydzielonych w poszczeg�lnych okr�gach}
  komitety   : array[1..l_kom] of char;              {Nazwy poszczeg�lnych komitet�w}

procedure wczytaj_dane; {Wczytanie danych do tablicy}
 var 
  nazwa_komitetu : char;
  dane           : text;      {Plik z danymi}
  i              : 1..l_okr;  {Indeks}
  j              : 1..l_kom;  {Indeks}
  k              : 0..l_kom;  {Indeks}
begin
  assign(dane, 'dane.txt');
  reset(dane);
  
  k := 0;
  for nazwa_komitetu:='A' to 'F' do
  begin
    k := k + 1;
    komitety[k] := nazwa_komitetu;
  end;
  
  for i := 1 to l_okr do
   begin
    for j := 1 to l_kom do 
      read(dane, glosy[i,j]);
    read(dane, l_mandatow[i]);
    readln(dane);
   end;
   
  close(dane);
end;

procedure mandaty;
 var 
  ktory   : integer;   {Kt�ry komitet ma dot�d najwy�szy wsp�czynnik v}
  max     : real;      {Ile wynosi dot�d najwy�szy wsp�czynnik v}
  v       : real;      {Warto�� wsp�czynnika v}
  i       : 1..l_okr;  {Indeks}
  j       : 1..l_kom;  {Indeks}
  k       : integer;   {Indeks} 

begin
  for i := 1 to l_okr do
    for j := 1 to l_kom do 
      mandat[i,j] := 0;
	  
  for i := 1 to l_okr do
   begin
    for k := 1 to l_mandatow[i] do {przydzielenie kolejnego mandatu}
     begin
       max   := 0;
       ktory := 1;
       for j := 1 to l_kom do 
        begin
         v := glosy[i,j] / (mandat[i,j]+1);
         if max < v then 
          begin
           max   := v;
           ktory := j;
          end;
        end; {for j}
      mandat[i,ktory] := mandat[i,ktory] + 1;
     end; {for k}
   end; {for i}
end; {mandaty}

procedure pkt1;
 var 
  suma : integer;   {Liczba g�os�w bie��cego komitetu}
  i    : 1..l_okr;  {Indeks}
  j    : 1..l_kom;  {Indeks}

begin
  writeln(wyn,'1');
  for j := 1 to l_kom do
   begin
    suma := 0;
    for i := 1 to l_okr do 
     suma := suma + glosy[i,j];
    writeln(wyn, komitety[j], '-', suma);
   end;
end;

procedure pkt2;
 var 
  suma      : integer;   {Liczba g�os�w w bie��cym  okr�gu}
  max, min  : integer;   {Najwi�ksza i najmniejsza dot�d liczba g�os�w w okr�gu}
  ktory_min, 
  ktory_max : 0..l_okr;  {Numery okr�g�w o najmniejszej i najwi�kszej liczbie g�os�w} 
  i         : 1..l_okr;  {Indeks}
  j         : 1..l_kom;  {Indeks}
begin
  writeln(wyn, '2');
  max := 0; 
  min := maxint;
  ktory_min := 0; 
  ktory_max := 0;
  for i := 1 to l_okr do
  begin
    suma := 0;
    for j := 1 to l_kom do
      suma := suma + glosy[i,j];
    if suma > max then 
	 begin 
	  max := suma; 
	  ktory_max := i; 
	 end;
    if suma < min then 
	 begin 
	  min := suma; 
	  ktory_min := i; 
	 end;
  end;
  writeln(wyn, 'min: okreg nr ', ktory_min);
  writeln(wyn, 'max: okreg nr ', ktory_max);
end;

procedure pkt3;
 const
  nr_okr = 6; {Dla tego komitetu liczymy liczb� mandat�w}
 var
  j : 1..l_kom;  {Indeks}
begin
  writeln(wyn, '3');
  for j := 1 to l_kom do 
    writeln(wyn, komitety[j], '-', mandat[nr_okr,j]);
end;

procedure pkt4;
 var
  suma : integer;   {Liczba mandat�w bie��cego komitetu}
  i    : 1..l_okr;  {Indeks}
  j    : 1..l_kom;  {Indeks}
begin
  writeln(wyn, '4');
  for j := 1 to l_kom do
   begin
    suma := 0;
    for i := 1 to l_okr do
      suma := suma + mandat[i,j];
    writeln(wyn, komitety[j], ' - ', suma);  
   end;
end;

begin {Program}
  wczytaj_dane;              {Wczytanie danych }
  
  mandaty;                   {Obliczenie liczby mandat�w}  
  
  assign(wyn, 'wybory.txt'); {Utworzenie}
  rewrite(wyn);              {pliku wynikowego}
  
  {Wyznaczanie i zapisywanie odpowiedzi do poszczeg�lnych podpunkt�w}
  pkt1;
  pkt2;
  pkt3;
  pkt4;
  
  close(wyn);
end.
