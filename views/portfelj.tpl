%rebase("base.tpl")

<h3> {{portfelj.ime}}  {{portfelj.vrednost_portfelja()}}</h3>
<table>
    <thead>
        <tr>
            <th> kratica </th>
            <th> polno ime </th>
            <th> kolicina </th>
            <th> cena enega </th>
            <th> skupna vrednost </th>
        </tr>
    </thead>
    <tbody>
        % for kovanec in portfelj.kovanci:
        <tr>
            <td> {{kovanec.kratica}} </td>
            <td> {{kovanec.polno_ime}} </td>
            <td> {{kovanec.kolicina}} </td>
            <td> {{kovanec.trenutna_cena_enega()}}</td>
        </tr>
        %end
    </tbody>



</table>

    <section>
    <h4> Dodajanje novega kovanca </h4>
    <i> v spodnji obrzec vnesite zahtevane podatke: </i>
        <p>
            
                <form method="POST" action="/dodaj-kovanec/{{ id_portfelja}}/">
                    <label>Kratica</label><br>
                    <input type="text" name="kratica"><br>
                    <label>Polno ime</label><br>
                    <input type="text" name="polno ime"><br>
                    <label>Posebnost kovanca</label><br>
                    <input type="text" name="posebnost"><br>
                    <label>Količina v lasti</label><br>
                    <input type="text" name="kolicina"><br>
                        <button>DODAJ</button>
                </form>
        </p>
    </section>


    
        
