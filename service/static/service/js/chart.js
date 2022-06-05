
      const data = {
        labels: [
          'Gampola',
          'Kandy',
          'Colombo',
          'Nawalapitiya',

        ],
        datasets: [{
          label: 'My First Dataset',
          data: [80, 50, 100, 100],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(255, 0, 155)'
          ],
          hoverOffset: 20
        }]
      };

      data2 = {
        labels: [
          'Monday',
          'Tuesday',
          'Wednesday',
          'Thursday',
          'Friday',
          'Saturday',
          'Sunday'

        ],
        datasets: [{
          label: 'Tea Wight(Kg)',
          data: [65, 70, 60, 80, 67, 87, 56],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(255, 0, 155)'
          ],
          hoverOffset: 4
        }]
      };


      //
      // Note: changes to the plugin code is not reflected to the chart,
      // because the plugin is loaded at chart construction time and editor
      // changes only trigger an chart.update().


      const plugin = {
        id: 'custom_canvas_background_color',
        beforeDraw: (chart) => {
          const ctx = chart.canvas.getContext('2d');
          ctx.save();
          ctx.globalCompositeOperation = 'destination-over';
          ctx.fillStyle = 'rgba(255, 255, 255, 0)';
          ctx.fillRect(0, 0, chart.width, chart.height);
          ctx.restore();
        }
      };


      // Config Block
      const config = {
        type: 'doughnut',
        data: data,
        options: {
          animation:{
            delay:500,
          },
        },
        plugins: [plugin],
      };



      // Second Chart Congig

      const config2 = {
        type: 'line',
        data: data2,
        options: {
          animation:{
            tension: {
              duration: 1500,
              easing: 'linear',
              from: 1,
              to: 0,
              loop: true
          },
            delay: 500,
          },
          borderWidth: 5,
          hoverRadius:10,
          pointStyle:'circle',
          responsive: true,
          maintainAspectRatio:false,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Tea Wight Over The Week'
            }
          }
        },
      };

      var inView = false;

      function isScrolledIntoView(elem)
      {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();

        var elemTop = $(elem).offset().top;
      var elemBottom = elemTop + $(elem).height();

      return ((elemTop <= docViewBottom) && (elemBottom >= docViewTop));
    }

    $(window).scroll(function() {
        if (isScrolledIntoView('#myChart2')) {
          if (inView) { return; }
          inView = true;
          console.log('')
          render();
          render2();
        } else {
          inView = false;
        }
      });

      // Render block
      function render(){
        const myChart = new Chart(
          document.getElementById('myChart'),
          config
        )
      }

      // Render Line Chart

      function render2(){ //
        const myChart2 = new Chart(
          document.getElementById('myChart2'),
          config2
        )
      }
