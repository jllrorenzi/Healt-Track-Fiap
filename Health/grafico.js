// create data
var data = [
    ["Janeiro", 80],
    ["Fevereiro", 77],
    ["Março", 75],
    ["Abril", 73],
    ["Maio", 70]
  ];
      

  chart = anychart.line();
  

  var series = chart.line(data);
  

  chart.container("grafico1");
  

  chart.draw();



  var data = [
    ["Jump", 25],
    ["Corrida", 50],
    ["Abdominal", 75],
    ["Corda", 100]
  ];
  

  chart = anychart.bar();
  

  var series = chart.bar(data);
  

  chart.container("grafico2");
  

  chart.draw();

  var data = [
    {x: "Gordura", value: 637166},
    {x: "Proteína", value: 721630},
    {x: "Carboidrato", value: 148662}
  ];
  

  chart = anychart.pie(data);
  
 
  chart.innerRadius("30%");
  

  chart.container("grafico3");
  

  chart.draw();
