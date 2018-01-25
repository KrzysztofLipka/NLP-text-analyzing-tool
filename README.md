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





<li>
creating virtualenv (virtualenv -p <path to python> virtual)</br>
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
change directory to repository folder:</br>
<strong>cd NLPtool</strong>
</li>


<li>
install requirements from textfile:</br>
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
run app:</br>
<strong>flask run</strong>
</li>


</ol>

<h2>Użyte technologie</h2>
<h3>Biblioteki NLP</h3>
<ul>
<li> <a href = "https://legacy.spacy.io/docs/">Spacy wersja</a></li>
<li> <a href = "http://www.nltk.org/">Nltk</a></li> 
<li> <a href = "https://radimrehurek.com/gensim/">Gensim</a></li> 
</ul>






