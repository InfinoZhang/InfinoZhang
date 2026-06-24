<script setup>
import { ref } from 'vue'
import {
  BarChart3,
  Check,
  CheckCircle,
  Clock,
  FileCheck,
  Image,
  Lock,
  Megaphone,
  ShieldCheck,
  Upload,
  Video,
} from '@lucide/vue'

import electronicsCaseVideo from './assets/case-electronics.mp4'
import skincareCaseVideo from './assets/case-skincare.mp4'
import foodCaseVideo from './assets/case-food.mp4'
import aromaCaseVideo from './assets/case-aroma.mp4'
import contactProductDrone from './assets/contact-product-drone.png'
import contactProductEarbuds from './assets/contact-product-earbuds.png'
import contactProductProjector from './assets/contact-product-projector.png'
import contactProductVacuum from './assets/contact-product-vacuum.png'
import heroShowreelVideo from './assets/hero-showreel.mp4'
import heroProductWall from './assets/hero-product-wall.jpg'
import infinoLogo from './assets/infino-logo.png'
import serviceAds from './assets/service-ads.jpg'
import serviceOperation from './assets/service-operation.jpg'
import serviceVideo from './assets/service-video.jpg'
import serviceVisual from './assets/service-visual.jpg'

const services = [
  {
    icon: Image,
    image: serviceVisual,
    title: 'AI 商品视觉',
    text: '白底图、生活方式场景图、电商主图、广告海报与多尺寸适配。',
  },
  {
    icon: Video,
    image: serviceVideo,
    title: 'AI 产品短视频',
    text: '6-15 秒产品动画、竖屏短视频、广告开场 Hook、字幕与结束页。',
  },
  {
    icon: Megaphone,
    image: serviceAds,
    title: '广告创意套装',
    text: '围绕功能卖点、使用场景、痛点解决、促销与高端感制作变体。',
  },
  {
    icon: BarChart3,
    image: serviceOperation,
    title: '内容代运营',
    text: '从选题、排期、素材更新到创意复盘，持续陪跑品牌内容生产。',
  },
]

const cases = [
  {
    video: electronicsCaseVideo,
    tag: '消费电子配件',
    title: '耳机产品从单品图扩展为电商卡片、社媒内容和广告素材',
    metrics: ['暗色科技感', '多触点展示', '品牌一致'],
  },
  {
    video: skincareCaseVideo,
    tag: '护肤美妆',
    title: '精华液产品快速生成详情页、广告图和短视频视觉方向',
    metrics: ['清透质感', '成分场景', '商用表达'],
  },
  {
    video: foodCaseVideo,
    tag: '饮料食品与营养品',
    title: '围绕口味、成分和货架卖点制作跨平台创意素材',
    metrics: ['包装真实', '广告变体', '数据表达'],
  },
  {
    video: aromaCaseVideo,
    tag: '香薰家居与日用消费品',
    title: '把香氛产品放入生活方式场景，强化氛围与购买动机',
    metrics: ['生活方式', '系列套装', '高端质感'],
  },
]

const benefits = [
  '更快上线新品与活动素材',
  '降低单个有效素材制作成本',
  '一次产出更多广告测试变体',
  '适配官网、电商、社媒和信息流广告',
  '人工质检产品外观、Logo、颜色和比例',
  '沉淀品牌视觉档案，减少重复沟通',
]

const workflow = [
  '提交产品与需求',
  '制定创意方向',
  'AI 生产与人工精修',
  '客户审核与修改',
  '多尺寸文件交付',
]

const plans = [
  {
    name: '单品创意验证包',
    price: '¥69 起',
    detail: '1 个 SKU，2 个创意方向，8 张图片，2 条短视频。',
    theme: 'white',
  },
  {
    name: '新品发布包',
    price: '按 SKU 报价',
    detail: '适合新品上架、电商详情页、社媒预热和广告首轮测试。',
    theme: 'gray',
  },
  {
    name: '月度创意订阅',
    price: '月度合作',
    detail: '为持续上新和持续投放团队提供稳定素材产能。',
    theme: 'black-gold',
  },
]

const safeguards = [
  { icon: ShieldCheck, title: '真实性校验', text: '检查包装文字、Logo、比例、颜色和材质表达。' },
  { icon: Lock, title: '资料保密', text: '产品图、品牌规范和参考资料仅用于项目交付。' },
  { icon: FileCheck, title: '明确交付', text: '交付格式、修改轮次、周期和 AI 使用边界提前说明。' },
  { icon: BarChart3, title: '转化追踪', text: '第一版重点关注案例浏览、表单提交和咨询转化。' },
]

const caseShowcaseProducts = [
  { image: contactProductDrone, alt: 'Infino Aero X1 产品展示图' },
  { image: contactProductProjector, alt: 'Infino Beam S 产品展示图' },
  { image: contactProductEarbuds, alt: 'Infino Pods Pro 产品展示图' },
  { image: contactProductVacuum, alt: 'Infino Clean One 产品展示图' },
]

const form = ref({
  company: '',
  name: '',
  email: '',
  phone: '',
  category: '',
  sku: '',
  assetType: '图片和视频',
  platform: 'Shopify / 独立站',
  timeline: '',
  budget: '500以下',
  note: '',
  botField: '',
})

const submitted = ref(false)
const submitting = ref(false)
const submitError = ref('')

async function submitBrief() {
  submitted.value = false
  submitError.value = ''

  if (form.value.botField) {
    return
  }

  submitting.value = true

  const payload = new URLSearchParams({
    'form-name': 'brief',
    subject: 'Infino 官网新需求',
    company: form.value.company,
    name: form.value.name,
    email: form.value.email,
    phone: form.value.phone,
    category: form.value.category,
    sku: form.value.sku,
    timeline: form.value.timeline,
    assetType: form.value.assetType,
    budget: form.value.budget,
    platform: form.value.platform,
    note: form.value.note,
    'bot-field': form.value.botField,
  })

  try {
    const response = await fetch('/__forms.html', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: payload.toString(),
    })

    if (!response.ok) {
      throw new Error('Form submission failed')
    }

    submitted.value = true
  } catch {
    submitError.value = '提交失败，请稍后重试，或直接通过邮箱联系我们。'
  } finally {
    submitting.value = false
  }
}

function playCaseVideo(event) {
  const video = event.currentTarget
  video.play().catch(() => {})
}

function resetCaseVideo(event) {
  const video = event.currentTarget
  video.pause()
  video.currentTime = 0
}

function toggleCaseVideo(event) {
  const video = event.currentTarget

  if (video.paused) {
    video.play().catch(() => {})
    return
  }

  video.pause()
}
</script>

<template>
  <div class="site-shell">
    <header class="topbar">
      <a class="brand" href="#top" aria-label="Infino 首页">
        <img class="brand-logo" :src="infinoLogo" alt="Infino" />
      </a>
      <nav aria-label="主导航">
        <a href="#cases">案例</a>
        <a href="#services">服务</a>
        <a href="#pricing">套餐</a>
        <a href="#brief">联系</a>
      </nav>
    </header>

    <main id="top">
      <section class="hero">
        <video
          class="hero-video"
          :src="heroShowreelVideo"
          :poster="heroProductWall"
          autoplay
          muted
          loop
          playsinline
          preload="auto"
          aria-hidden="true"
        ></video>
        <div class="hero-content">
          <h1 class="hero-title" data-text="无界映像 Infino">无界映像 Infino</h1>
          <p class="hero-slogan">让每一个产品，都拥有无限表达</p>
          <p class="hero-copy">
            让产品离开安静的白底图，走进可被看见、被记住、被点击的场景里。Infino 用 AI 与人工创意，把一个 SKU 延展成一组完整的视觉叙事：有质感的商品图、有节奏的短视频，也有为广告测试准备的多种创意方向。
          </p>
        </div>
        <div class="hero-proof" aria-label="首版官网核心指标">
          <span>3-5 天交付</span>
          <span>2 轮修改</span>
          <span>多平台适配</span>
        </div>
      </section>

      <section id="cases" class="section">
        <div class="section-heading">
          <h2 class="section-art-title">案例</h2>
          <p class="section-description">用真实行业样片展示 Infino 如何把产品变成可投放创意资产。</p>
        </div>
        <div class="case-showcase" aria-label="产品展示图">
          <img v-for="product in caseShowcaseProducts" :key="product.alt" :src="product.image" :alt="product.alt" loading="lazy" decoding="async" />
        </div>
        <div class="case-grid">
          <article v-for="item in cases" :key="item.title" class="case-card">
            <video
              class="case-media"
              :src="item.video"
              :aria-label="`${item.tag} 商品视觉案例`"
              muted
              playsinline
              preload="metadata"
              @mouseenter="playCaseVideo"
              @mouseleave="resetCaseVideo"
              @click="toggleCaseVideo"
            ></video>
            <div class="case-content">
              <span>{{ item.tag }}</span>
              <h3>{{ item.title }}</h3>
              <ul>
                <li v-for="metric in item.metrics" :key="metric">
                  <Check :size="16" />
                  {{ metric }}
                </li>
              </ul>
            </div>
          </article>
        </div>
      </section>

      <section id="services" class="section split-band">
        <div class="section-heading">
          <h2 class="section-art-title">服务</h2>
          <p class="section-description">从商品视觉、短视频、广告创意到内容代运营，为品牌提供持续、稳定、可交付的创意生产支持。</p>
        </div>
        <div class="service-grid">
          <article v-for="service in services" :key="service.title" class="service-item">
            <img class="service-media" :src="service.image" :alt="`${service.title} 服务示意图`" loading="lazy" decoding="async" />
            <component :is="service.icon" :size="26" />
            <h3>{{ service.title }}</h3>
            <p>{{ service.text }}</p>
          </article>
        </div>
      </section>

      <section class="section benefits">
        <div class="section-heading">
          <h2>
            <span>更快上线</span>
            <span>更低成本</span>
            <span>更多可测试素材。</span>
          </h2>
        </div>
        <div class="benefit-list">
          <div v-for="benefit in benefits" :key="benefit">
            <CheckCircle :size="20" />
            <span>{{ benefit }}</span>
          </div>
        </div>
      </section>

      <section class="section workflow">
        <div class="section-heading">
          <h2>
            <span>把复杂工具链藏在后面，</span>
            <span>把交付标准放到前面。</span>
          </h2>
        </div>
        <ol>
          <li v-for="(step, index) in workflow" :key="step">
            <span>{{ String(index + 1).padStart(2, '0') }}</span>
            <strong>{{ step }}</strong>
          </li>
        </ol>
      </section>

      <section id="pricing" class="section pricing">
        <div class="section-heading">
          <h2>从小单开始，快速验证创意效果。</h2>
        </div>
        <div class="plan-grid">
          <article v-for="plan in plans" :key="plan.name" class="plan-card" :class="`plan-card-${plan.theme}`">
            <h3>{{ plan.name }}</h3>
            <strong>{{ plan.price }}</strong>
            <p>{{ plan.detail }}</p>
          </article>
        </div>
      </section>

      <section class="section safeguards">
        <div class="section-heading">
          <h2>放心商用，清楚交付，减少返工。</h2>
        </div>
        <div class="safeguard-grid">
          <article v-for="item in safeguards" :key="item.title" class="safeguard-item">
            <component :is="item.icon" :size="24" />
            <h3>{{ item.title }}</h3>
            <p>{{ item.text }}</p>
          </article>
        </div>
      </section>

      <section id="brief" class="section brief-section">
        <div class="brief-heading">
          <h2 class="brief-title">联系我们</h2>
          <div class="brief-contact-list" aria-label="联系邮箱和电话">
            <span>邮箱：InfinoZhang@outlook.com</span>
            <span>邮箱：zhang01670615@163.com</span>
            <span>电话：15755564721</span>
          </div>
        </div>
        <div class="brief-copy">
          <div class="brief-visual" aria-label="联系我们产品场景图"></div>
        </div>

        <form
          class="brief-form"
          name="brief"
          method="POST"
          data-netlify="true"
          netlify-honeypot="bot-field"
          @submit.prevent="submitBrief"
        >
          <input type="hidden" name="form-name" value="brief" />
          <input type="hidden" name="subject" value="Infino 官网新需求" />
          <p hidden>
            <label>
              请不要填写此字段
              <input v-model="form.botField" name="bot-field" />
            </label>
          </p>
          <label>
            企业名称
            <input v-model="form.company" name="company" required placeholder="例如：Infino Beauty" />
          </label>
          <label>
            姓名
            <input v-model="form.name" name="name" required placeholder="例如：张先生" />
          </label>
          <label>
            邮箱
            <input v-model="form.email" name="email" type="email" placeholder="例如：name@example.com" />
          </label>
          <label>
            电话
            <input v-model="form.phone" name="phone" type="tel" placeholder="例如：138 0000 0000" />
          </label>
          <label>
            产品品类
            <input v-model="form.category" name="category" placeholder="护肤、美妆、食品、家居..." />
          </label>
          <div class="form-row">
            <label>
              SKU 数量
              <input v-model="form.sku" name="sku" placeholder="例如：1-5 个" />
            </label>
            <label>
              交付时间
              <input v-model="form.timeline" name="timeline" type="date" />
            </label>
          </div>
          <div class="form-row">
            <label>
              需要内容
              <select v-model="form.assetType" name="assetType">
                <option>图片和视频</option>
                <option>仅图片</option>
                <option>仅视频</option>
              </select>
            </label>
            <label>
              预算范围
              <select v-model="form.budget" name="budget">
                <option>500以下</option>
                <option>500-1000</option>
                <option>1000以上</option>
              </select>
            </label>
          </div>
          <label>
            目标平台
            <input v-model="form.platform" name="platform" placeholder="Shopify / Amazon / TikTok / 小红书..." />
          </label>
          <label>
            产品图与品牌资料说明
            <textarea v-model="form.note" name="note" rows="4" placeholder="可写产品链接、资料情况、参考风格或投放目标。" />
          </label>
          <button class="button primary form-button" type="submit" :disabled="submitting">
            <Upload :size="18" />
            {{ submitting ? '提交中...' : '联系我们' }}
          </button>
          <p v-if="submitted" class="form-success">
            已收到这次需求，我们会尽快查看并联系你。
          </p>
          <p v-if="submitError" class="form-error">
            {{ submitError }}
          </p>
        </form>
      </section>
    </main>

    <footer class="footer">
      <span>Infino · AI 企业官网 MVP</span>
      <span><Clock :size="16" /> 先服务，后软件</span>
    </footer>
  </div>
</template>
