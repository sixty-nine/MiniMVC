<%inherit file="layout.mako"/>

<div class="about">
    <h2>About MiniMVC</h2>
    <p>MiniMVC is a Python micro MVC framework inspired by Symfony2 from the PHP world.</p>
    <ul>
        <li>MiniMVC is lightweighted</li>
        <li>MiniMVC uses dependency injection</li>
        <li>MiniMVC is configured with YAML</li>
        <li>MiniMVC is tested (partially)</li>
    </ul>
    
    <p>MiniMVC features:</p>
    <ul>
        <li>A configurable service container</li>
        <li>A flexible and configurable request router based on pyroutes</li>
        <li>Powerful logging mechanism based on logbook</li>
        <li>Basic SQL Alchemy binding</li>
        <li>Cheetah and Mako templates, new templating engines can be added very easily</li>
    </ul>
    
    <p>TODO</p>
    <ul>
        <li>Write more tests</li>
        <li>Reorganize imports</li>
        <li>Configure SQLAlchemy with the ServiceContainer</li>
        <ul>
            <li>Generate table classes</li>
            <li>Generate entities</li>
        </ul>
        <li>Read XML configuration in addition to yaml</li>
        <li>More templating engines</li>
        <li>...</li>
    </ul>
</div>

<div class="about">
    <h2>About the author</h2>
    <p>I am not an experienced Python programmer so please forgive me if MiniMVC is not state of the art code. I started MiniMVC just for fun and to learn mod_python :-)</p>
    <p>Feel free to contact me with your feedback about MiniMVC or if you want to contribute to make it better. I will mantain MiniMVC if there is some interest out there.</p>
</div>

<div>
    <h2>Demo</h2>
    <ul>
        <b>View Layer</b>
        <li><a href="/mako">Mako templates</a></li>
        <li><a href="/cheetah">Cheetah templates</a></li>
    </ul>
</div>