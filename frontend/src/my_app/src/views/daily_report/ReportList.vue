<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>日報一覧</h1>
        <v-container>
          <v-row v-for="report in reports" :key="report.id">
            <v-col cols="10">
              <v-card class="mx-auto">
                <v-card-text>
                  <p class="text-h4 text--primary">
                    {{ report.target_date }}の日報
                  </p>
                  <v-row>
                    <div
                      v-for="tag in report.tags"
                      :key="tag.id"
                      class="d-flex flex-wrap justify-start"
                    >
                      <v-chip color="blue" outlined pill class="ml-1 mt-1d">{{
                        tag.name
                      }}</v-chip>
                    </div>
                  </v-row>
                  <p class="text-h5 text--primary pt-3">内容</p>
                  <div class="text--primary">{{ report.content }}</div>
                  <p class="text-h5 text--primary pt-3">
                    気付き、初めて知ったこと
                  </p>
                  <div class="text--primary">{{ report.notice }}</div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12"></v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "../../components/layouts/AppBar.vue";
export default {
  name: "ReportList",
  components: {
    AppBar,
  },
  data() {
    return {
      reports: [],
      auth: [],
      accessToken: null,
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.getReports();
  },
  methods: {
    async getReports() {
      await this.axios
        .get("http://0.0.0.0:8000/api/daily_report/index/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          this.reports = response.data;
          console.log(this.reports);
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
  },
};
</script>