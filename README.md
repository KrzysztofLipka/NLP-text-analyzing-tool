<h2>Aplikacja stworzona dla pracy inżynierskiej:
Wykorzystanie w webowym edytorze JavaScript bibliotek programistycznych do przetwarzania języka naturalnego (np. NLTK).
</h2> 
<p>autor : Krzysztof Lipka</p>
<p>Uruchamianie pracy:</p>  
<ul>
<li>1.Należy uruchomić plik app.py </li>  
<li>2.Wpisać w pasku adresu http://127.0.0.1:5000/</l1> 
</ul>
<h2>Moduły w projekcie:</h2> 
<ul>
<li>app.py - moduł zawierajacy kontrolery które odbierają żądania z edytora.
i następnie wywołują odpowiednie usługi.</li>  
<li>word_click_models - funkcje odpowiedzialne za zwracanie synonimów
słów podobnych klikniętego słowa oraz częsci mowy dla klikniętego zdania.</li>
<li>text_update_models - funkcje uruchamiane po zmianie wartości zmiennej stanu edytora.
zwraca najpopularniejsze słowa wraz z ich liczebnością.</li>
<li>folder training zawiera moduły związane z obsługa zbiorów danych, które nastepnie są używane do uczenia maszynowego.</li>  
<li>folder ml_models zawiera zapisane, wyuczne modele.</li>  
</ul>

<h2>Użyte technologie</h2>
<h3>Biblioteki NLP</h3>
<ul>
<li> <a href = "https://legacy.spacy.io/docs/">Spacy wersja 1.9</a></li>
<li> <a href = "http://www.nltk.org/">Nltk 3.2.4</a></li> 
<li> <a href = "https://radimrehurek.com/gensim/">Gensim 3.0.1</a></li> 
</ul>

<h3>Interpreter</h3>
<ul>
<li>Anaconda 3 dla Python w wersji 3.5</li> 
</ul>





