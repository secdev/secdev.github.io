/*
 * Create the scapy version table
 */

google.charts.load('current', {'packages':['table']});
google.charts.setOnLoadCallback(drawTable);

function drawTable() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Scapy version');
  data.addColumn('number', 'Python 2.2-2.6');
  data.addColumn('number', 'Python 2.7');
  data.addColumn('number', 'Python 3.4-3.6');
  data.addColumn('number', 'Python 3.7');
  data.addColumn('number', 'Python 3.8');
  var y = {v: 1, f: "YES"};
  var n = {v: 0, f: "NO"}; 
  data.addRows([
    ['2.2.X',       y, y, n, n, n],
    ['2.3.3',       y, y, n, n, n],
    ['2.4.0',       n, y, y, n, n],
    ['2.4.2',       n, y, y, y, n],
    ['2.4.3-2.4.4', n, y, y, y, y]
  ]);
  var formatter = new google.visualization.ColorFormat();
  formatter.addRange(0.5, 1.5, '#2E9AFE', '#2E9AFE');  // Python 2
  formatter.addRange(-0.5, 0.5, '#848484', '#848484');
  for (let i = 1; i <= 2; i++) {
    formatter.format(data, i);
  }

  var formatter = new google.visualization.ColorFormat();
  formatter.addRange(0.5, 1.5, '#FA5858', '#FA5858');  // Python 3
  formatter.addRange(-0.5, 0.5, '#848484', '#848484');
  for (let i = 3; i <= 5; i++) {
    formatter.format(data, i);
  }

  var table = new google.visualization.Table(document.getElementById('table_div'));
  var options = {
    allowHtml: true,
    showRowNumber: false,
    sort: 'disable',
    width: '600px',
    height: '150px'
  }

  table.draw(data, options);
}
