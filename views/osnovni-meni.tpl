% rebase("base.tpl")
    
    % if stevilo_portfeljev == 0:
    <p>
        <b> V navigacijski vrstici lahko ustvarite nove porftfelje! <br> </b>
         Podrobnejša navodila za uporabo porgrama pa najdete pod zavihkom navodila.
    </p>
    % else:
    <p> <b> Število tvojih portfeljev: {{stevilo_portfeljev}}</b> </p>
    <p> <i> na tej strani je prikazan hiter pregled portfeljev </i></p>
    
    


        %for id_portfelja, portfelj in enumerate(portfelji):
        <article>
            <h5><mark>{{portfelj.ime.upper()}}</mark></h5>
                
            
                <table>
                    <thead>
                        <tr>
                            <th>Kratica</th>
                            <th>Kolicina v lasti</th>
                        </tr>
                    </thead>
                    
                    <tbody>
                    %for kovanec in portfelj.kovanci:
                        <tr>
                            <td>{{kovanec.kratica}}</td>
                            <td>{{kovanec.kolicina}}</td>
                        </tr>
                    %end
                    </tbody>
                </table>
             
        <a href="/portfelj/{{id_portfelja}}/"><button>podrobnejše informacije o portfelju</button></a>    
        </article>
        %end
          
        </article>
    


