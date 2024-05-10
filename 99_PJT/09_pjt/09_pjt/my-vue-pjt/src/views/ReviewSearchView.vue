<template>
  <!-- 유튜브 검색과 검색 결과를 표시하는 컴포넌트 -->
  <div>
    <!-- 검색 입력 필드 -->
    <input type="text" v-model="searchTarget">
    <!-- 검색 버튼 -->
    <button @click="searchYT">검색</button>

    <!-- 검색 결과를 나타내는 비디오들 -->
    <div v-for="video in videos.items" :key="video.id.videoId" class="video-container">
      <!-- 비디오를 클릭하면 모달 열기 -->
      <div @click="openModal(video)">
        <!-- 썸네일 이미지 -->
        <div class="img-container">
          <img :src="video.snippet.thumbnails.default.url" alt="">
        </div>
        <!-- 비디오 제목과 설명 -->
        <div class="text-container">
          <p>{{ video.snippet.title }}</p>
          <p>{{ video.snippet.description }}</p>
        </div>
        <hr> <!-- 구분선 -->
      </div>
    </div>
    
    <!-- 유튜브 리뷰 모달 컴포넌트 -->
    <YoutubeReviewModal :video="selectedVideo" :modalOn="modalOn" @modalOff="offModal" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue'

// 검색어와 검색 결과를 저장하는 변수들
const searchTarget = ref('')
const videos = ref('')
const selectedVideo = ref(null)
const modalOn = ref(false)

// 유튜브 검색을 위한 함수
const searchYT = function() {
  const API_KEY = import.meta.env.VITE_YT_API_KEY

  axios({
    method: 'get',
    url: `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}`,
    params: {
      part: 'snippet',
      q: searchTarget.value,
      maxResults: 10,
      type: 'video',
    }
  })
    .then((response) => {
      videos.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

// 모달을 열기 위한 함수
const openModal = function (video) {
  selectedVideo.value = video
  modalOn.value = true
}

// 모달을 닫기 위한 함수
const offModal = function (){
  modalOn.value = false
}

</script>

<style scoped>
/* 비디오 컨테이너 스타일 */
.video-container{
  display: flex;
  align-items: center;
}
/* 썸네일 컨테이너 스타일 */
.img-container{
  flex: 0 0 auto;
  margin-right: 20px;
}

/* 텍스트 컨테이너 스타일 */
.text-container{
  flex: 1;
}
/* 구분선 스타일 */
hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 20px 0;
}
</style>
