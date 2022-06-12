<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>目標を更新する</h1>
        <v-container>
          <v-row>
            <v-col cols="7" class="white">
              <v-form ref="form" v-model="valid" lazy-validation class="ml-10">
                <v-container fluid>
                  <v-checkbox
                    v-model="check"
                    label="目標を完了にする"
                  ></v-checkbox>
                  <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="date"
                        label="完了日"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="date"
                      no-title
                      scrollable
                      locale="ja-jp"
                    >
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu = false">
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(date)"
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                  <v-text-field
                    v-model="targetName"
                    :rules="targetRules"
                    label="目標"
                  ></v-text-field>
                </v-container>
                <v-btn
                  :disabled="!valid"
                  color="success"
                  @click="validate"
                  class="ml-4"
                >
                  更新
                </v-btn>
              </v-form>
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
  name: "EditTarget",
  components: {
    AppBar,
  },
  data() {
    return {
      valid: true,
      targetRules: [(v) => !!v || "内容を入力してください"],
      auth: [],
      accessToken: null,
      userId: null,
      targetName: null,
      targetId: null,
      completed_at: null,
      target: [],
      menu: null,
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      check: true,
    };
  },
  mounted() {
    this.targetId = this.$route.params.targetId;
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.userId = this.auth.id;
    this.getTarget();
  },
  methods: {
    async getTarget() {
      await this.axios
        .get(
          "http://0.0.0.0:8000/api/target_management/" + this.targetId + "/",
          {
            headers: { Authorization: "JWT " + this.accessToken },
          }
        )
        .then((response) => {
          console.log(response);
          this.target = response.data;
          this.targetName = this.target.name;
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },

    async validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        await this.axios
          .put(
            "http://0.0.0.0:8000/api/target_management/" + this.targetId + "/",
            {
              user: this.userId,
              name: this.targetName,
              completed_at: this.date,
              status: this.check,
            },
            { headers: { Authorization: "JWT " + this.accessToken } }
          )
          .then((response) => {
            console.log(response);
          })
          .catch((e) => {
            console.log("目標更新に失敗しました", e);
            console.log(e.request);
          });
      }
    },
  },
};
</script>
<style scoped>
.v-text-field {
  width: 400px;
}
</style>