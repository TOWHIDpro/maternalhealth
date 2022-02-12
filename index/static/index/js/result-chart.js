let app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
      return{
        x: {
          type: 'bar',
          data: {
              labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
              datasets: [{
                  label: '# of Votes',
                  data: [1, 1, 2, 0, 0, 2],
                  backgroundColor: [
                      'rgba(255, 99, 132, 0.2)',
                      'rgba(54, 162, 235, 0.2)',
                      'rgba(255, 206, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(153, 102, 255, 0.2)',
                      'rgba(255, 159, 64, 0.2)'
                  ],
                  borderColor: [
                      'rgba(255, 99, 132, 1)',
                      'rgba(54, 162, 235, 1)',
                      'rgba(255, 206, 86, 1)',
                      'rgba(75, 192, 192, 1)',
                      'rgba(153, 102, 255, 1)',
                      'rgba(255, 159, 64, 1)'
                  ],
                  borderWidth: 1
              }]
          },
          options: {
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
        }
      }
    },
    mounted() {
      this.showchart()
    },
    methods: {
      showchart(){
        const ctx = document.getElementById('myChart').getContext('2d')
        const myChart = new Chart(ctx, this.x)
        this.myChart = myChart
        
      },
      changeChart(name){
        this.x.type = name
        this.myChart.destroy()
        this.showchart()

      }
    }
})