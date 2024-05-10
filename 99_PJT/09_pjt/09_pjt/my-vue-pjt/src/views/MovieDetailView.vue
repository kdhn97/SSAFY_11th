<template>
  <!-- 영화 상세 정보를 표시하는 컴포넌트입니다. -->
  <div class="detail">
    <!-- 영화 포스터를 표시합니다. -->
    <img :src="imgSrc">

    <h3>{{ movie.title }}</h3>
    <p>개봉일 : {{ movie.release_date }}</p>
    <p>러닝타임 : {{ movie.runtime }}분</p>
    <p>TMDB 평점 : {{ movie.vote_average }}</p>
    <h3>장르</h3>
    <p v-for="genre in movie.genres">{{ genre.name }}</p>
    <h3>줄거리</h3>
    <p>{{ movie.overview }}</p>
    <h3>공식 예고편</h3>
    <!-- 유튜브 예고편 버튼 -->
    <button @click="youtube"><img src="https://t3.ftcdn.net/jpg/04/74/05/94/360_F_474059464_qldYuzxaUWEwNTtYBJ44VN89ARuFktHW.jpg" width=100px alt=""></button>
  
    <!-- 유튜브 예고편 모달 -->
    <div class="modal" v-if="modalOn" @click="modalOff">
      <div class="modal-content" @click.stop>
        <button @click="modalOff">x</button>
        <div class="modal-title">{{ video.items[0].snippet.title }}</div>
        <div class="modal-body">
          <iframe width="560" height="315" :src="videoUrl" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios';

// 현재 라우트를 사용합니다.
const route = useRoute()
// 현재 영화의 ID를 저장하는 변수입니다.
const movieId = ref(route.params.movieId)
// 영화 정보를 저장하는 변수입니다.
const movie = ref('')
// 영화 포스터 이미지의 URL을 저장하는 변수입니다.
const imgSrc = ref('')

// 유튜브 검색 결과를 저장하는 변수입니다.
const video = ref('')
// 모달 상태를 나타내는 변수입니다.
const modalOn = ref(false)

// 영화 상세 정보를 가져오는 함수입니다.
const movieDetail = function() {
  // TMDB API 키를 가져옵니다.
  const API_KEY = import.meta.env.VITE_TMDB_API_KEY
  // TMDB API를 사용하여 영화 상세 정보를 가져옵니다.
  axios({
    method: 'get',
    url: `https://api.themoviedb.org/3/movie/${movieId.value}`,
    params: {
      api_key: API_KEY,
      language: 'ko-KR'
    }
  })
  .then((response) => {
    // API 요청이 성공하면 영화 정보를 변수에 저장합니다.
    movie.value = response.data
    // 영화 포스터 이미지의 URL을 생성하여 변수에 저장합니다.
    imgSrc.value = `https://image.tmdb.org/t/p/w500/${response.data.poster_path}`
  })
  .catch((error) => {
    console.log(error);
  })
}

// 유튜브 API 키를 가져옵니다.
const API_KEY = import.meta.env.VITE_YT_API_KEY
// 유튜브 예고편을 검색하는 함수입니다.
const youtube = function () {
  // 모달을 열기
  modalOn.value = true
  // 유튜브 API를 사용하여 검색합니다.
  axios({
    method: 'get',
    url: `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}`,
    params: {
      part: 'snippet',
      q: movie.value.title + '리뷰',
      maxResults: 1,
      type: 'video',
    }
  })
    .then((response) => {
      // API 요청이 성공하면 검색 결과를 변수에 저장합니다.
      video.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

// 모달을 닫는 함수입니다.
const modalOff = function () {
  modalOn.value = false
}

// 비디오의 URL을 생성하는 계산된 속성입니다.
const videoUrl = computed(() => {
  if (video.value.items[0].id.videoId) {
    return `https://www.youtube.com/embed/${video.value.items[0].id.videoId}`
  }
})

// 페이지가 마운트될 때 영화 상세 정보를 가져오는 함수를 실행합니다.
onMounted(() => {
  movieDetail()
})
</script>

<style scoped>
/* 영화 상세 정보 스타일 */
.detail {
  text-align: center;
}
/* 모달 스타일 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color:rgba(0, 0, 0, 0.205);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 모달 내용 스타일 */
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  max-width: 80%;
  max-height: 80%;
  overflow-y: auto; 
}

/* 모달 제목 스타일 */
.modal-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

/* 모달 본문 스타일 */
.modal-body {
  font-size: 16px;
}
</style>
