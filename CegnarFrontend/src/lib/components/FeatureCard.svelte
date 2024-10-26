<script>
    export let knifeImg;
    export let textureImg;
    export let flipped;
    export let heading;
    export let description;
    export let buttonText;

    import FireImg from "../static/images/fire-texture.jpg";
</script>

<div class="flex h-80 overflow-hidden rounded-2xl hover:border-white border-transparent border-[0.5px] transition-all duration-200 feature-card mb-10" class:flipped>
    <div class="h-full w-3/6 relative bg-contain card-images">
        <img src={textureImg} class:-left-16={!flipped} class="absolute rotate-[-30deg] w-full max-w-[500px] h-[200%] -top-16 opacity-60" alt="">
        <img src={knifeImg} alt="" class:left-0={!flipped} class="absolute top-1/2 translate-y-[-50%] w-full transition-all duration-200">
    </div>
    
    <div class="text-textSecondary text-end flex items-center pe-4 card-text relative">
        <div class="">
            <h1 class="text-4xl font-heading text-textPrimary">{heading}</h1>
            <p class="mb-10 w-5/6 ms-auto">{description}</p>
            <a href="/kontakt" class="btn">Zanima me</a>
        </div>
        <img src={FireImg} alt="" class="absolute opacity-15 -right-32 -top-52 -rotate-12">
    </div>
</div>