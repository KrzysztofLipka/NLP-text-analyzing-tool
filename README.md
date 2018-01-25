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
<li>Create a new folder:</br>
<strong>mkdir project</strong>
</li>





<li>
creating virtualenv (virtualenv -p <path to python> virtual)</br>
<strong>virtualenv -p C:\Python36\python.exe virtual</strong>
</li>


<li>
Activate virtualenv:
<strong>virtual\Scripts\activate</strong>
</li>


<li>
Clone repository:
<strong>git clone https://github.com/KrzysztofLipka/Django_website NLPtool</strong>
</li>


<li>
change directory to repository folder:
<strong>cd NLPtool</strong>
</li>


<li>
install requirements from textfile:
<strong>pip install -r requirements.txt</strong>
</li>


<li>
Activate virtualenv:
<strong>virtual\Scripts\activate</strong>
</li>

<li>
Download corpuses for NLTK:
<strong>python -m nltk.downloader wordnet averaged_perceptron_tagger punkt</strong>
</li>

<li>
Set flask app (export command for linux):
<strong>set FLASK_APP=__init__.py</strong>
</li>

<li>
run app:
<strong>flask run</strong>
</li>

<li>text_update_models - funkcje uruchamiane po zmianie wartości zmiennej stanu edytora.
zwraca najpopularniejsze słowa wraz z ich liczebnością.</li>
<li>folder training zawiera moduły związane z obsługa zbiorów danych, które nastepnie są używane do uczenia maszynowego.</li>  
<li>folder ml_models zawiera zapisane, wyuczne modele.</li>  
</ol>

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





