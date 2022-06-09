<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>タグ一覧</h1>
        <v-container>
          <v-row>
            <!-- <v-col height="200" v-for="tag in tags" :key="tag.id" cols="2">
              <v-chip color="blue" link outlined pill>{{ tag.name }}</v-chip>
            </v-col> -->
            <v-col cols="8" class="white d-flex flex-wrap">
              <v-chip
                color="blue"
                link
                outlined
                pill
                v-for="tag in tags"
                :key="tag.id"
                class="ml-3 mt-3"
                >{{ tag.name }}</v-chip
              >
            </v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "../../components/layouts/AppBar.vue";
export default {
  name: "TagList",
  components: {
    AppBar,
  },
  data() {
    return {
      tags: [],
    };
  },
  mounted() {
    this.getTags();
  },
  methods: {
    async getTags() {
      const data = await this.axios
        .get("http://0.0.0.0:8000/api/tag/index/")
        .then((response) => {
          console.log(response);
          this.tags = response.data;
        })
        .catch((e) => {
          console.log("エラー", e);
        });
      console.log(data);
    },
  },
};
</script>