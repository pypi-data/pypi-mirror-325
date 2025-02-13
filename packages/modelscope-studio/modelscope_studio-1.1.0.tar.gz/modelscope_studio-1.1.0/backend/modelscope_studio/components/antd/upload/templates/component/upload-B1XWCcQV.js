import { i as Le, a as K, r as Se, g as Fe, w as A, b as Ue } from "./Index-DS517vxE.js";
const C = window.ms_globals.React, ue = window.ms_globals.React.useMemo, Re = window.ms_globals.React.forwardRef, de = window.ms_globals.React.useRef, fe = window.ms_globals.React.useState, pe = window.ms_globals.React.useEffect, H = window.ms_globals.ReactDOM.createPortal, ke = window.ms_globals.internalContext.useContextPropsContext, V = window.ms_globals.internalContext.ContextPropsProvider, Ce = window.ms_globals.antd.Upload;
var Oe = /\s/;
function Te(e) {
  for (var t = e.length; t-- && Oe.test(e.charAt(t)); )
    ;
  return t;
}
var Pe = /^\s+/;
function je(e) {
  return e && e.slice(0, Te(e) + 1).replace(Pe, "");
}
var $ = NaN, Ne = /^[-+]0x[0-9a-f]+$/i, We = /^0b[01]+$/i, Ae = /^0o[0-7]+$/i, De = parseInt;
function ee(e) {
  if (typeof e == "number")
    return e;
  if (Le(e))
    return $;
  if (K(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = K(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = je(e);
  var o = We.test(e);
  return o || Ae.test(e) ? De(e.slice(2), o ? 2 : 8) : Ne.test(e) ? $ : +e;
}
function Me() {
}
var B = function() {
  return Se.Date.now();
}, ze = "Expected a function", qe = Math.max, Be = Math.min;
function Ge(e, t, o) {
  var i, s, n, r, c, u, h = 0, I = !1, l = !1, _ = !0;
  if (typeof e != "function")
    throw new TypeError(ze);
  t = ee(t) || 0, K(o) && (I = !!o.leading, l = "maxWait" in o, n = l ? qe(ee(o.maxWait) || 0, t) : n, _ = "trailing" in o ? !!o.trailing : _);
  function f(p) {
    var b = i, F = s;
    return i = s = void 0, h = p, r = e.apply(F, b), r;
  }
  function y(p) {
    return h = p, c = setTimeout(g, t), I ? f(p) : r;
  }
  function d(p) {
    var b = p - u, F = p - h, W = t - b;
    return l ? Be(W, n - F) : W;
  }
  function m(p) {
    var b = p - u, F = p - h;
    return u === void 0 || b >= t || b < 0 || l && F >= n;
  }
  function g() {
    var p = B();
    if (m(p))
      return L(p);
    c = setTimeout(g, d(p));
  }
  function L(p) {
    return c = void 0, _ && i ? f(p) : (i = s = void 0, r);
  }
  function w() {
    c !== void 0 && clearTimeout(c), h = 0, i = u = s = c = void 0;
  }
  function a() {
    return c === void 0 ? r : L(B());
  }
  function S() {
    var p = B(), b = m(p);
    if (i = arguments, s = this, u = p, b) {
      if (c === void 0)
        return y(u);
      if (l)
        return clearTimeout(c), c = setTimeout(g, t), f(u);
    }
    return c === void 0 && (c = setTimeout(g, t)), r;
  }
  return S.cancel = w, S.flush = a, S;
}
var me = {
  exports: {}
}, q = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var He = C, Ke = Symbol.for("react.element"), Je = Symbol.for("react.fragment"), Xe = Object.prototype.hasOwnProperty, Ye = He.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Qe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function we(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Xe.call(t, i) && !Qe.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Ke,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Ye.current
  };
}
q.Fragment = Je;
q.jsx = we;
q.jsxs = we;
me.exports = q;
var z = me.exports;
const {
  SvelteComponent: Ze,
  assign: te,
  binding_callbacks: ne,
  check_outros: Ve,
  children: _e,
  claim_element: he,
  claim_space: $e,
  component_subscribe: re,
  compute_slots: et,
  create_slot: tt,
  detach: j,
  element: Ie,
  empty: oe,
  exclude_internal_props: ie,
  get_all_dirty_from_scope: nt,
  get_slot_changes: rt,
  group_outros: ot,
  init: it,
  insert_hydration: D,
  safe_not_equal: st,
  set_custom_element_data: ge,
  space: ct,
  transition_in: M,
  transition_out: J,
  update_slot_base: lt
} = window.__gradio__svelte__internal, {
  beforeUpdate: at,
  getContext: ut,
  onDestroy: dt,
  setContext: ft
} = window.__gradio__svelte__internal;
function se(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = tt(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = Ie("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = he(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = _e(t);
      s && s.l(r), r.forEach(j), this.h();
    },
    h() {
      ge(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      D(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && lt(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? rt(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : nt(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (M(s, n), o = !0);
    },
    o(n) {
      J(s, n), o = !1;
    },
    d(n) {
      n && j(t), s && s.d(n), e[9](null);
    }
  };
}
function pt(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && se(e)
  );
  return {
    c() {
      t = Ie("react-portal-target"), o = ct(), n && n.c(), i = oe(), this.h();
    },
    l(r) {
      t = he(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), _e(t).forEach(j), o = $e(r), n && n.l(r), i = oe(), this.h();
    },
    h() {
      ge(t, "class", "svelte-1rt0kpf");
    },
    m(r, c) {
      D(r, t, c), e[8](t), D(r, o, c), n && n.m(r, c), D(r, i, c), s = !0;
    },
    p(r, [c]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, c), c & /*$$slots*/
      16 && M(n, 1)) : (n = se(r), n.c(), M(n, 1), n.m(i.parentNode, i)) : n && (ot(), J(n, 1, 1, () => {
        n = null;
      }), Ve());
    },
    i(r) {
      s || (M(n), s = !0);
    },
    o(r) {
      J(n), s = !1;
    },
    d(r) {
      r && (j(t), j(o), j(i)), e[8](null), n && n.d(r);
    }
  };
}
function ce(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function mt(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const c = et(n);
  let {
    svelteInit: u
  } = t;
  const h = A(ce(t)), I = A();
  re(e, I, (a) => o(0, i = a));
  const l = A();
  re(e, l, (a) => o(1, s = a));
  const _ = [], f = ut("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: d,
    subSlotIndex: m
  } = Fe() || {}, g = u({
    parent: f,
    props: h,
    target: I,
    slot: l,
    slotKey: y,
    slotIndex: d,
    subSlotIndex: m,
    onDestroy(a) {
      _.push(a);
    }
  });
  ft("$$ms-gr-react-wrapper", g), at(() => {
    h.set(ce(t));
  }), dt(() => {
    _.forEach((a) => a());
  });
  function L(a) {
    ne[a ? "unshift" : "push"](() => {
      i = a, I.set(i);
    });
  }
  function w(a) {
    ne[a ? "unshift" : "push"](() => {
      s = a, l.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = te(te({}, t), ie(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = ie(t), [i, s, I, l, c, u, r, n, L, w];
}
class wt extends Ze {
  constructor(t) {
    super(), it(this, t, mt, pt, st, {
      svelteInit: 5
    });
  }
}
const le = window.ms_globals.rerender, G = window.ms_globals.tree;
function _t(e, t = {}) {
  function o(i) {
    const s = A(), n = new wt({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const c = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? G;
          return u.nodes = [...u.nodes, c], le({
            createPortal: H,
            node: G
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((h) => h.svelteInstance !== s), le({
              createPortal: H,
              node: G
            });
          }), c;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
function ht(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function It(e, t = !1) {
  try {
    if (Ue(e))
      return e;
    if (t && !ht(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function x(e, t) {
  return ue(() => It(e, t), [e, t]);
}
const gt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function vt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = yt(o, i), t;
  }, {}) : {};
}
function yt(e, t) {
  return typeof t == "number" && !gt.includes(e) ? t + "px" : t;
}
function X(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: c
        } = X(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: c,
          children: [...C.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(H(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: c,
      useCapture: u
    }) => {
      o.addEventListener(c, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: c
      } = X(n);
      t.push(...c), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function bt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const xt = Re(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = de(), [c, u] = fe([]), {
    forceClone: h
  } = ke(), I = h ? !0 : t;
  return pe(() => {
    var y;
    if (!r.current || !e)
      return;
    let l = e;
    function _() {
      let d = l;
      if (l.tagName.toLowerCase() === "svelte-slot" && l.children.length === 1 && l.children[0] && (d = l.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), bt(n, d), o && d.classList.add(...o.split(" ")), i) {
        const m = vt(i);
        Object.keys(m).forEach((g) => {
          d.style[g] = m[g];
        });
      }
    }
    let f = null;
    if (I && window.MutationObserver) {
      let d = function() {
        var w, a, S;
        (w = r.current) != null && w.contains(l) && ((a = r.current) == null || a.removeChild(l));
        const {
          portals: g,
          clonedElement: L
        } = X(e);
        l = L, u(g), l.style.display = "contents", _(), (S = r.current) == null || S.appendChild(l);
      };
      d();
      const m = Ge(() => {
        d(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      f = new window.MutationObserver(m), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      l.style.display = "contents", _(), (y = r.current) == null || y.appendChild(l);
    return () => {
      var d, m;
      l.style.display = "", (d = r.current) != null && d.contains(l) && ((m = r.current) == null || m.removeChild(l)), f == null || f.disconnect();
    };
  }, [e, I, o, i, n, s]), C.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...c);
});
function ae(e, t) {
  return e ? /* @__PURE__ */ z.jsx(xt, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function P({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ z.jsx(V, {
    params: s,
    forceClone: !0,
    children: ae(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ z.jsx(V, {
    params: s,
    forceClone: !0,
    children: ae(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const Et = (e) => !!e.name;
function Rt(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const St = _t(({
  slots: e,
  upload: t,
  showUploadList: o,
  progress: i,
  beforeUpload: s,
  customRequest: n,
  previewFile: r,
  isImageUrl: c,
  itemRender: u,
  iconRender: h,
  data: I,
  onChange: l,
  onValueChange: _,
  onRemove: f,
  maxCount: y,
  fileList: d,
  setSlotParams: m,
  ...g
}) => {
  const L = e["showUploadList.downloadIcon"] || e["showUploadList.removeIcon"] || e["showUploadList.previewIcon"] || e["showUploadList.extra"] || typeof o == "object", w = Rt(o), a = x(w.showPreviewIcon), S = x(w.showRemoveIcon), p = x(w.showDownloadIcon), b = x(s), F = x(n), W = x(i == null ? void 0 : i.format), ve = x(r), ye = x(c), be = x(u), xe = x(h), Ee = x(I), N = de(!1), [U, Y] = fe(d);
  pe(() => {
    Y(d);
  }, [d]);
  const Q = ue(() => (U == null ? void 0 : U.map((v) => Et(v) ? v : {
    ...v,
    name: v.orig_name || v.path,
    uid: v.uid || v.url || v.path,
    status: "done"
  })) || [], [U]);
  return /* @__PURE__ */ z.jsx(Ce, {
    ...g,
    fileList: Q,
    data: Ee || I,
    previewFile: ve,
    isImageUrl: ye,
    maxCount: 1,
    itemRender: e.itemRender ? P({
      slots: e,
      setSlotParams: m,
      key: "itemRender"
    }) : be,
    iconRender: e.iconRender ? P({
      slots: e,
      setSlotParams: m,
      key: "iconRender"
    }) : xe,
    onRemove: (v) => {
      if (N.current)
        return;
      f == null || f(v);
      const O = Q.findIndex((k) => k.uid === v.uid), R = U.slice();
      R.splice(O, 1), _ == null || _(R), l == null || l(R.map((k) => k.path));
    },
    customRequest: F || Me,
    beforeUpload: async (v, O) => {
      if (b && !await b(v, O) || N.current)
        return !1;
      N.current = !0;
      let R = O;
      if (typeof y == "number") {
        const E = y - U.length;
        R = O.slice(0, E < 0 ? 0 : E);
      } else if (y === 1)
        R = O.slice(0, 1);
      else if (R.length === 0)
        return N.current = !1, !1;
      Y((E) => [...y === 1 ? [] : E, ...R.map((T) => ({
        ...T,
        size: T.size,
        uid: T.uid,
        name: T.name,
        status: "uploading"
      }))]);
      const k = (await t(R)).filter((E) => E), Z = y === 1 ? k : [...U.filter((E) => !k.some((T) => T.uid === E.uid)), ...k];
      return N.current = !1, _ == null || _(Z), l == null || l(Z.map((E) => E.path)), !1;
    },
    progress: i && {
      ...i,
      format: W
    },
    showUploadList: L ? {
      ...w,
      showDownloadIcon: p || w.showDownloadIcon,
      showRemoveIcon: S || w.showRemoveIcon,
      showPreviewIcon: a || w.showPreviewIcon,
      downloadIcon: e["showUploadList.downloadIcon"] ? P({
        slots: e,
        setSlotParams: m,
        key: "showUploadList.downloadIcon"
      }) : w.downloadIcon,
      removeIcon: e["showUploadList.removeIcon"] ? P({
        slots: e,
        setSlotParams: m,
        key: "showUploadList.removeIcon"
      }) : w.removeIcon,
      previewIcon: e["showUploadList.previewIcon"] ? P({
        slots: e,
        setSlotParams: m,
        key: "showUploadList.previewIcon"
      }) : w.previewIcon,
      extra: e["showUploadList.extra"] ? P({
        slots: e,
        setSlotParams: m,
        key: "showUploadList.extra"
      }) : w.extra
    } : o
  });
});
export {
  St as Upload,
  St as default
};
