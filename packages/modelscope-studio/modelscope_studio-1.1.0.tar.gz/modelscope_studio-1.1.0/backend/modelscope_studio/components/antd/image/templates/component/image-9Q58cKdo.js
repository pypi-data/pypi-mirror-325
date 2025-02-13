import { i as de, a as A, r as fe, g as me, w as k, b as pe } from "./Index-DAgRlmcj.js";
const y = window.ms_globals.React, se = window.ms_globals.React.forwardRef, le = window.ms_globals.React.useRef, ce = window.ms_globals.React.useState, ae = window.ms_globals.React.useEffect, ue = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, z = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Image;
var ge = /\s/;
function we(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var ve = /^\s+/;
function be(e) {
  return e && e.slice(0, we(e) + 1).replace(ve, "");
}
var B = NaN, ye = /^[-+]0x[0-9a-f]+$/i, xe = /^0b[01]+$/i, Ce = /^0o[0-7]+$/i, Ee = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return B;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = be(e);
  var r = xe.test(e);
  return r || Ce.test(e) ? Ee(e.slice(2), r ? 2 : 8) : ye.test(e) ? B : +e;
}
var L = function() {
  return fe.Date.now();
}, Ie = "Expected a function", Re = Math.max, Se = Math.min;
function ke(e, t, r) {
  var s, i, n, o, l, u, p = 0, g = !1, c = !1, v = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = G(t) || 0, A(r) && (g = !!r.leading, c = "maxWait" in r, n = c ? Re(G(r.maxWait) || 0, t) : n, v = "trailing" in r ? !!r.trailing : v);
  function m(d) {
    var b = s, S = i;
    return s = i = void 0, p = d, o = e.apply(S, b), o;
  }
  function x(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : o;
  }
  function f(d) {
    var b = d - u, S = d - p, U = t - b;
    return c ? Se(U, n - S) : U;
  }
  function _(d) {
    var b = d - u, S = d - p;
    return u === void 0 || b >= t || b < 0 || c && S >= n;
  }
  function h() {
    var d = L();
    if (_(d))
      return C(d);
    l = setTimeout(h, f(d));
  }
  function C(d) {
    return l = void 0, v && s ? m(d) : (s = i = void 0, o);
  }
  function E() {
    l !== void 0 && clearTimeout(l), p = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? o : C(L());
  }
  function I() {
    var d = L(), b = _(d);
    if (s = arguments, i = this, u = d, b) {
      if (l === void 0)
        return x(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), o;
  }
  return I.cancel = E, I.flush = a, I;
}
var ee = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = y, Te = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Fe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, r) {
  var s, i = {}, n = null, o = null;
  r !== void 0 && (n = "" + r), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (s in t) je.call(t, s) && !Fe.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Te,
    type: e,
    key: n,
    ref: o,
    props: i,
    _owner: Le.current
  };
}
j.Fragment = Pe;
j.jsx = te;
j.jsxs = te;
ee.exports = j;
var w = ee.exports;
const {
  SvelteComponent: Ne,
  assign: H,
  binding_callbacks: K,
  check_outros: We,
  children: ne,
  claim_element: re,
  claim_space: Ae,
  component_subscribe: q,
  compute_slots: Me,
  create_slot: De,
  detach: R,
  element: oe,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Ue,
  get_slot_changes: ze,
  group_outros: Be,
  init: Ge,
  insert_hydration: O,
  safe_not_equal: He,
  set_custom_element_data: ie,
  space: Ke,
  transition_in: T,
  transition_out: M,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function X(e) {
  let t, r;
  const s = (
    /*#slots*/
    e[7].default
  ), i = De(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var o = ne(t);
      i && i.l(o), o.forEach(R), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(n, o) {
      O(n, t, o), i && i.m(t, null), e[9](t), r = !0;
    },
    p(n, o) {
      i && i.p && (!r || o & /*$$scope*/
      64) && qe(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        r ? ze(
          s,
          /*$$scope*/
          n[6],
          o,
          null
        ) : Ue(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      r || (T(i, n), r = !0);
    },
    o(n) {
      M(i, n), r = !1;
    },
    d(n) {
      n && R(t), i && i.d(n), e[9](null);
    }
  };
}
function Qe(e) {
  let t, r, s, i, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), r = Ke(), n && n.c(), s = V(), this.h();
    },
    l(o) {
      t = re(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(R), r = Ae(o), n && n.l(o), s = V(), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      O(o, t, l), e[8](t), O(o, r, l), n && n.m(o, l), O(o, s, l), i = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? n ? (n.p(o, l), l & /*$$slots*/
      16 && T(n, 1)) : (n = X(o), n.c(), T(n, 1), n.m(s.parentNode, s)) : n && (Be(), M(n, 1, 1, () => {
        n = null;
      }), We());
    },
    i(o) {
      i || (T(n), i = !0);
    },
    o(o) {
      M(n), i = !1;
    },
    d(o) {
      o && (R(t), R(r), R(s)), e[8](null), n && n.d(o);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function Ze(e, t, r) {
  let s, i, {
    $$slots: n = {},
    $$scope: o
  } = t;
  const l = Me(n);
  let {
    svelteInit: u
  } = t;
  const p = k(Y(t)), g = k();
  q(e, g, (a) => r(0, s = a));
  const c = k();
  q(e, c, (a) => r(1, i = a));
  const v = [], m = Je("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: _
  } = me() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(a) {
      v.push(a);
    }
  });
  Ye("$$ms-gr-react-wrapper", h), Ve(() => {
    p.set(Y(t));
  }), Xe(() => {
    v.forEach((a) => a());
  });
  function C(a) {
    K[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function E(a) {
    K[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    r(17, t = H(H({}, t), J(a))), "svelteInit" in a && r(5, u = a.svelteInit), "$$scope" in a && r(6, o = a.$$scope);
  }, t = J(t), [s, i, g, c, l, u, o, n, C, E];
}
class $e extends Ne {
  constructor(t) {
    super(), Ge(this, t, Ze, Qe, He, {
      svelteInit: 5
    });
  }
}
const Q = window.ms_globals.rerender, F = window.ms_globals.tree;
function et(e, t = {}) {
  function r(s) {
    const i = k(), n = new $e({
      ...s,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, u = o.parent ?? F;
          return u.nodes = [...u.nodes, l], Q({
            createPortal: W,
            node: F
          }), o.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== i), Q({
              createPortal: W,
              node: F
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(r);
    });
  });
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const s = e[r];
    return t[r] = rt(r, s), t;
  }, {}) : {};
}
function rt(e, t) {
  return typeof t == "number" && !tt.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const i = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(W(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: l,
      useCapture: u
    }) => {
      r.addEventListener(l, o, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = D(n);
      t.push(...l), r.appendChild(o);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function ot(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const P = se(({
  slot: e,
  clone: t,
  className: r,
  style: s,
  observeAttributes: i
}, n) => {
  const o = le(), [l, u] = ce([]), {
    forceClone: p
  } = _e(), g = p ? !0 : t;
  return ae(() => {
    var x;
    if (!o.current || !e)
      return;
    let c = e;
    function v() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), ot(n, f), r && f.classList.add(...r.split(" ")), s) {
        const _ = nt(s);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var E, a, I;
        (E = o.current) != null && E.contains(c) && ((a = o.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: C
        } = D(e);
        c = C, u(h), c.style.display = "contents", v(), (I = o.current) == null || I.appendChild(c);
      };
      f();
      const _ = ke(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", v(), (x = o.current) == null || x.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = o.current) != null && f.contains(c) && ((_ = o.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, r, s, n, i]), y.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function it(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function st(e, t = !1) {
  try {
    if (pe(e))
      return e;
    if (t && !it(e))
      return;
    if (typeof e == "string") {
      let r = e.trim();
      return r.startsWith(";") && (r = r.slice(1)), r.endsWith(";") && (r = r.slice(0, -1)), new Function(`return (...args) => (${r})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function N(e, t) {
  return ue(() => st(e, t), [e, t]);
}
function lt(e) {
  return Object.keys(e).reduce((t, r) => (e[r] !== void 0 && (t[r] = e[r]), t), {});
}
function Z(e, t) {
  return e ? /* @__PURE__ */ w.jsx(P, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function $({
  key: e,
  slots: t,
  targets: r
}, s) {
  return t[e] ? (...i) => r ? r.map((n, o) => /* @__PURE__ */ w.jsx(z, {
    params: i,
    forceClone: !0,
    children: Z(n, {
      clone: !0,
      ...s
    })
  }, o)) : /* @__PURE__ */ w.jsx(z, {
    params: i,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
function ct(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const ut = et(({
  slots: e,
  preview: t,
  setSlotParams: r,
  children: s,
  ...i
}) => {
  const n = ct(t), o = e["preview.mask"] || e["preview.closeIcon"] || e["preview.toolbarRender"] || e["preview.imageRender"] || t !== !1, l = N(n.getContainer), u = N(n.toolbarRender), p = N(n.imageRender);
  return /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [/* @__PURE__ */ w.jsx("div", {
      style: {
        display: "none"
      },
      children: s
    }), /* @__PURE__ */ w.jsx(he, {
      ...i,
      preview: o ? lt({
        ...n,
        getContainer: l,
        toolbarRender: e["preview.toolbarRender"] ? $({
          slots: e,
          setSlotParams: r,
          key: "preview.toolbarRender"
        }) : u,
        imageRender: e["preview.imageRender"] ? $({
          slots: e,
          setSlotParams: r,
          key: "preview.imageRender"
        }) : p,
        ...e["preview.mask"] || Reflect.has(n, "mask") ? {
          mask: e["preview.mask"] ? /* @__PURE__ */ w.jsx(P, {
            slot: e["preview.mask"]
          }) : n.mask
        } : {},
        closeIcon: e["preview.closeIcon"] ? /* @__PURE__ */ w.jsx(P, {
          slot: e["preview.closeIcon"]
        }) : n.closeIcon
      }) : !1,
      placeholder: e.placeholder ? /* @__PURE__ */ w.jsx(P, {
        slot: e.placeholder
      }) : i.placeholder
    })]
  });
});
export {
  ut as Image,
  ut as default
};
