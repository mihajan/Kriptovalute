% rebase("base.tpl")

<header>
            <h2>Sledilec cen kriptovalut</h2>
            <p> program, ki vam prikaže vaše portfelje, pripadajoče kripto kovance in njihove vrednosti </p>
</header>
    
    
    % if stevilo_portfeljev == 0:
    <p>
        <b> V zavihku navodila si oglejte kako ustvarite svoje portfelje! </b>
    </p>
    % else:
    <p> <b> Število tvojih portfeljev: {{stevilo_portfeljev}}</b> </p>
    <p> <i> na tej strani vidiš svoje portfelje in kovance ki jih imaš dodane na njih </i></p>
    
    


        %for portfelj in portfelji:
        <article>
            <h5><mark>{{portfelj.ime.upper()}}</mark></h5>
                
        %for kovanec in portfelj.kovanci:
                <table>
                    <thead>
                        <tr>
                            <th>Kratica</th>
                            <th>Kolicina v lasti</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{{kovanec.kratica}}</td>
                            <td>{{kovanec.kolicina}}</td>
                        </tr>
                    </tbody>
                </table> 
            <a href="/portfelj/"><button>podrobnejše informacije o portfelju</button></a>    
        </article>
        %end
        
    


