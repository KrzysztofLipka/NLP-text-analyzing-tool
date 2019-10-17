
<h2>Aplikacja stworzona dla pracy inżynierskiej:
Wykorzystanie w webowym edytorze JavaScript bibliotek programistycznych do przetwarzania języka naturalnego (np. NLTK).
</h2> 
<p>autor : Krzysztof Lipka</p>
<p>Uruchamianie pracy:</p>  
<ol>
<li>Należy uruchomić plik app.py </li>  
<li>Wpisać w pasku adresu http://127.0.0.1:5000/</l1> 
</ol>
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
=======
<h2>An application that uses Natural Language Processing libraries in Web text editor</h2> 
<p>author : Krzysztof Lipka</p>
<p>Requirements:</p>  
<ul>
<li>Python 3.6 </li>  
<li>For Windows: Visual C++ 2015 Build Tools<a href = "http://landinghub.visualstudio.com/visual-cpp-build-tools">[link]</a></li> 
<li>Git</li>

</ul>
<h2>Instalation (on Windows):</h2> 
<ol>
  
  
<li>Create a new folder:(using cmd)</br>
<strong>mkdir project</strong>
</li>

<li>Change directory</br>
<strong>cd project</strong>
</li>




<li>
Creating virtualenv (virtualenv -p <path to python> virtual)</br>
<strong>virtualenv -p C:\Python36\python.exe virtual</strong>
</li>


<li>
Activate virtualenv:</br>
<strong>virtual\Scripts\activate</strong>
</li>


<li>
Clone repository:</br>
<strong>git clone https://github.com/KrzysztofLipka/Django_website NLPtool</strong>
</li>


<li>
Change directory to repository folder:</br>
<strong>cd NLPtool</strong>
</li>


<li>
Install requirements from textfile:</br>
<strong>pip install -r requirements.txt</strong>
</li>


<li>
Activate virtualenv:</br>
<strong>virtual\Scripts\activate</strong>
</li>

<li>
Download corpuses for NLTK:</br>
<strong>python -m nltk.downloader wordnet averaged_perceptron_tagger punkt</strong>
</li>

<li>
Set flask app (export command for linux):</br>
<strong>set FLASK_APP=__init__.py</strong>
</li>

<li>
Run app:</br>
<strong>flask run</strong>
</li>


</ol>


<h3>NLP libraries</h3>
<ul>
<li> <a href = "https://spacy.io/">Spacy</a></li>
<li> <a href = "http://www.nltk.org/">Nltk</a></li> 
<li> <a href = "https://radimrehurek.com/gensim/">Gensim</a></li> 
</ul>

<h3>Files in project</h3>
<p>...</p>

<h3>Todo:</h3>
<ol>
<li>More useful and responsive frontend</li>
<li>Tool for fining relations between entities in text</li>
<li>Functions for training new models that can be easy to use and customize</li>
</ol>




