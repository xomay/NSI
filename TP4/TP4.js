function question1(){
  const reponse = document.quizz.question1.value;
  return reponse=="Pu sa mère";
}
function question2() {
  const reponse = document.quizz.question2.value;
  return reponse=="1";
}
function question3() {
  const reponse = document.getElementsByName('question3');
  return (reponse[0].checked) && (reponse[1].checked) && (reponse[2].checked) &&(reponse[3].checked)
  && (reponse[4].checked) && (!reponse[5].checked) && (reponse[6].checked) && (reponse[7].checked)
}
function score() {
  let res=0;
  if (question1()){
    res++;
    alert("question 1 : Bravo !");
  }
  else{
    alert("question 1 : la bonne réponse était pu sa mère");
  }
  if (question2()){
    res++;
    alert("question 2 : Bravo !");
  }
  else{
    alert("question 2 : la bonne réponse était 1");
  }
  if (question3()){
    res++;
    alert("question 3 : Bravo !");
  }
  else{
    alert("question 3 : la bonne réponse était Mathys");
  }

  alert("Votre score est de "+ res + "point(s)");
}
