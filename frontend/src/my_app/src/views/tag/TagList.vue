<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>タグ一覧</h1>
        <div class="search">
          <v-text-field
            type="text"
            v-model="keyword"
            label="検索"
          ></v-text-field>
        </div>
        <v-container>
          <v-row>
            <v-col cols="10" class="white d-flex flex-wrap">
              <v-chip
                color="blue"
                link
                outlined
                pill
                v-for="tag in filteredTags"
                :key="tag.id"
                class="ml-3 mt-3"
                :to="{ name: 'TagDatail', params: { tagId: tag.id } }"
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
      keyword: "",
      auth: [],
      accessToken: null,
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    console.log(this.accessToken);
    this.getTags();
  },
  methods: {
    async getTags() {
      await this.axios
        .get("http://0.0.0.0:8000/api/tag/index/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          console.log(response);
          this.tags = response.data;
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
  },
  computed: {
    filteredTags() {
      let tags = [];
      for (let i in this.tags) {
        let tag = this.tags[i];
        if (tag.name.indexOf(this.keyword) !== -1) {
          tags.push(tag);
        }
      }
      return tags;
    },
  },
};
</script>