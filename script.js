function calculate() {
    var twdAmount = document.getElementById("twdAmount").value;
    
    if (isNaN(twdAmount) || twdAmount <= 0) {/*第五小題*/
      alert("請輸入有效數值！");
      reset();
      return;
    }
    
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      var rates = xhr.responseXML.getElementsByTagName("rate");
      var resultDiv = document.getElementById("result");
      resultDiv.innerHTML = "";
        
      for (var i = 0; i < rates.length; i++) {
        var currency = rates[i].getElementsByTagName("currency")[0].textContent;
        var rate = rates[i].getElementsByTagName("cashselling")[0].textContent;
        var convertedAmount = (twdAmount / rate).toFixed(2);
        var result = document.createElement("p");
        result.textContent = "轉換成 " + currency + ": " + convertedAmount + " " + currency;
        resultDiv.appendChild(result);
      }
    };
    xhr.open("GET", "rate.xml", true);
    xhr.send();
  }
  
  function reset() {/*第四小題*/
    document.getElementById("twdAmount").value = "";
    document.getElementById("result").innerHTML = "";
  }
  
