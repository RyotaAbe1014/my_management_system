<script>
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  data() {
    return {
      datas: {
        labels: ["完了", "未完了"],
        datasets: [
          {
            data: [this.completedTargetCount, this.inCompletedTargetCount],
            backgroundColor: ["#89c3eb", "#f87979"],
          },
        ],
      },
      options: {
        responsive: true,
      },
    };
  },
  props: {
    width: {
      type: Number,
      // default: 400,
    },
    height: {
      type: Number,
      // default: 400,
    },
    completedTargetCount: {
      type: Number,
    },
    inCompletedTargetCount: {
      type: Number,
    },
  },
  updated() {
    this.datas.datasets[0].data[0] = this.completedTargetCount;
    this.datas.datasets[0].data[1] = this.inCompletedTargetCount;
    this.renderChart(this.datas, this.options);
  },
  methods: {
    createChart() {
      this.$forceUpdate();
    },
  },
};
</script>