%rebase("base.tpl")

<h3> {{portfelj.ime}} </h3>

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
            <td> {{kovanec.trenutna_cena_enega()}} </td>
            <td> {{kovanec.trenutna_vrednost_dolocenega_kovanca()}} </td>       
        </tr>
        %end
    </tbody>
</table>

