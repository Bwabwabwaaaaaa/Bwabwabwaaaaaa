//On initialise des variables compteurs qui vont stocker le nombre de réponses correspondant au profil
var psycopathe=0;
var sociopathe=0;
var nevropathe=0;


//Fonction qui sera exécutée lors du clic sur le bouton valider du formulaire
function valider() {
	//On commence par récupérer la valeur du bouton radio qui a été coché par l'utilisateur 
	var perso= document.getElementById("personalite");
	var perso_choisi = perso.options[perso.selectedIndex].value;
	
	// Ensuite on ajoute la valeur dans la variable correspondante 
	// Par exemple si l'utilisateur a choisi expelliarmus alors on ajoute 1 à la variable griffondor
	if(perso_choisi=="p")
	{
		psycopathe=psycopathe+1;
	}
	else if(perso_choisi=="s")
	{
		sociopathe=sociopathe+1;
	}
	else
	{
		nevropathe=nevropathe+1;
	}
	
	//On regroupe les différents profils dans un tableau 
	var valeurs=[psycopathe,sociopathe,nevropathe,rien];
	var profils=["Psycopathe, tu es quelqu'un qu'il faut tenir à l'écart de la sociétée","Sociopathe, tu est quelqu'un qu'il faut tenir à l'écart de la sociétée","Nevropathe, tu es triste, tu le sais et tu le fais savoir au monde","vraiment indécis, tu sais qu'il faut choisir ?"];
	
	//On cherche le maximum du tableau et son indice
	var max = valeurs[0];
    var indice_du_max = 0;
    
    for (var i = 1; i < valeurs.length; i++) {
        if (valeurs[i] > max) {
            indice_du_max = i;
            max = valeurs[i];
        }
    }
	
	//on affiche le profil qui a eu le maximum de réponses dans la balise à l'identifiant resultat
	document.getElementById("resultat").innerHTML= "Félicitation ! Tu es un "+ profils[indice_du_max]
}

