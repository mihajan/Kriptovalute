% rebase("base.tpl")

<header>
            <h2>Sledilec cen kriptovalut</h2>
            <p> program, ki vam prikaže vaše portfelje, pripadajoče kripto kovance in njihove vrednosti </p>
</header>
    
    <p>
    % if stevilo_portfeljev == 0:
        <b> V zavihku navodila si oglejte kako ustvarite svoje portfelje! </b>
    % else:
        <b> Že imaš ustvarjenih toliko protfeljev: {{stevilo_portfeljev}}</b>
    </p>
    
    <ul> Imena protfeljev so: 
        %for portfelj in portfelji:
            <li> <strong> {{portfelj.ime}}</strong>; število kovancev na njem: {{portfelj.stevilo_razlicnih_kovancev()}}</li>     
                %for kovanec in portfelj.kovanci:
                <ul>
                    <li> {{kovanec.kratica}} </li>
                </ul>
        %end
        
    </ul>


