<script>
    export let knifeImg;
    export let textureImg;
    export let flipped;
    export let heading;
    export let description;
    // export let buttonText;

    import FireImg from "../static/images/fire-texture.jpg";
</script>

<div class="flex justify-between md:h-80 h-64 overflow-hidden rounded-2xl hover:border-white border-transparent border-[0.5px] transition-all duration-200 feature-card mb-10" class:flipped>
    <div class="h-full w-5/6 lg:w-3/6 relative bg-contain card-images block">
        <img src={textureImg} class:-left-16={!flipped} class="absolute rotate-[-30deg] w-full max-w-[500px] h-[200%] -top-16 -left-10 opacity-60" alt="">
        <img src={knifeImg} alt="" class:left-0={!flipped} class="absolute md:rotate-0 -rotate-90 md:bottom-0 md:scale-100 scale-[1.4] bottom-1/4 md:top-1/2 translate-y-[-50%] w-full transition-all duration-200">
    </div>
    
    <div class="text-textSecondary text-end flex items-center pe-4 pb-4 md:pb-0 md:w-4/6 w-full card-text relative">
        <div class="z-20">
            <h1 class="md:text-4xl text-2xl font-heading text-textPrimary">{heading}</h1>
            <p class="md:mb-10 mb-6 md:w-5/6 w-full ms-auto text-end md:text-base text-sm md:ms-auto">{@html description}</p>
            <a href="/kontakt" class="btn btn-">Zanima me</a>
        </div>
        <img src={FireImg} alt="" class="z-0 absolute opacity-15 -right-32 -top-52 2xl:-top-1/2 2xl:right-0 2xl:w-1/2 -rotate-12">
    </div>
</div>
